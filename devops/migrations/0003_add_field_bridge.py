# -*- coding: utf-8 -*-
# flake8: noqa
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Interface.bridge'
        db.add_column('devops_interface', 'bridge',
                      self.gf('django.db.models.fields.CharField')(
                          max_length=256, null=True), keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Interface.bridge'
        db.delete_column('devops_interface', 'bridge')

    models = {
        u'devops.address': {
            'Meta': {'object_name': 'Address'},
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.related.ForeignKey', [],
                          {'to': u"orm['devops.Interface']"}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [],
                           {'max_length': '39'})
        },
        u'devops.diskdevice': {
            'Meta': {'object_name': 'DiskDevice'},
            'bus': ('django.db.models.fields.CharField',
                    [], {'max_length': '255'}
                    ),
            'device': ('django.db.models.fields.CharField', [],
                       {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [],
                     {'to': u"orm['devops.Node']"}),
            'target_dev': ('django.db.models.fields.CharField', [],
                           {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'}),
            'volume': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['devops.Volume']", 'null': 'True'})
        },
        u'devops.environment': {
            'Meta': {'object_name': 'Environment'},
            'created': ('django.db.models.fields.DateTimeField', [],
                        {'default': 'datetime.datetime.utcnow',
                         'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '255'})
        },
        u'devops.interface': {
            'Meta': {'object_name': 'Interface'},
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'mac_address': ('django.db.models.fields.CharField', [],
                            {'unique': 'True', 'max_length': '255'}),
            'model': ('django.db.models.fields.CharField', [],
                      {'max_length': '255'}),
            'network': ('django.db.models.fields.related.ForeignKey', [],
                        {'to': u"orm['devops.Network']", 'null': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [],
                     {'to': u"orm['devops.Node']"}),
            'type': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'}),
            'bridge': ('django.db.models.fields.CharField', [],
                       {'unique': 'False', 'max_length': '255','null': 'True'}),
        },
        u'devops.network': {
            'Meta': {'unique_together': "(('name', 'environment'),)",
                     'object_name': 'Network'},
            'created': ('django.db.models.fields.DateTimeField', [],
                        {'default': 'datetime.datetime.utcnow',
                         'auto_now_add': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [],
                            {'to': u"orm['devops.Environment']",
                             'null': 'True'}),
            'forward': ('django.db.models.fields.CharField', [],
                        {'max_length': '255', 'null': 'True'}),
            'has_dhcp_server': ('django.db.models.fields.BooleanField', [],
                                {}),
            'has_pxe_server': ('django.db.models.fields.BooleanField', [], {}),
            'has_reserved_ips': ('django.db.models.fields.BooleanField', [],
                                 {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'ip_network': ('django.db.models.fields.CharField', [],
                           {'unique': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'}),
            'tftp_root_dir': ('django.db.models.fields.CharField', [],
                              {'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'})
        },
        u'devops.node': {
            'Meta': {'unique_together': "(('name', 'environment'),)",
                     'object_name': 'Node'},
            'architecture': ('django.db.models.fields.CharField', [],
                             {'max_length': '255'}),
            'boot': ('django.db.models.fields.CharField', [],
                     {'default': "'[]'", 'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [],
                        {'default': 'datetime.datetime.utcnow',
                         'auto_now_add': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [],
                            {'to': u"orm['devops.Environment']",
                             'null': 'True'}),
            'has_vnc': ('django.db.models.fields.BooleanField', [],
                        {'default': 'True'}),
            'hypervisor': ('django.db.models.fields.CharField', [],
                           {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'memory': ('django.db.models.fields.IntegerField', [],
                       {'default': '1024'}),
            'metadata': ('django.db.models.fields.CharField', [],
                         {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'}),
            'os_type': ('django.db.models.fields.CharField', [],
                        {'max_length': '255'}),
            'role': ('django.db.models.fields.CharField', [],
                     {'max_length': '255', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'}),
            'vcpu': ('django.db.models.fields.PositiveSmallIntegerField', [],
                     {'default': '1'})
        },
        u'devops.volume': {
            'Meta': {'unique_together': "(('name', 'environment'),)",
                     'object_name': 'Volume'},
            'backing_store': ('django.db.models.fields.related.ForeignKey', [],
                              {'to': u"orm['devops.Volume']", 'null': 'True'}),
            'capacity': ('django.db.models.fields.BigIntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [],
                        {'default': 'datetime.datetime.utcnow',
                         'auto_now_add': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [],
                            {'to': u"orm['devops.Environment']",
                             'null': 'True'}),
            'format': ('django.db.models.fields.CharField', [],
                       {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [],
                    {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [],
                     {'max_length': '255'})
        }
    }

    complete_apps = ['devops']
