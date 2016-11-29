# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Item'
        db.delete_table('author_item')


    def backwards(self, orm):
        # Adding model 'Item'
        db.create_table('author_item', (
            ('image', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alias', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('author', ['Item'])


    models = {
        'author.blogpost': {
            'Meta': {'object_name': 'Blogpost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'author.item2': {
            'Meta': {'object_name': 'Item2'},
            'alias': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['author']