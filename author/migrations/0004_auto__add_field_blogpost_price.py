# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blogpost.price'
        db.add_column('author_blogpost', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blogpost.price'
        db.delete_column('author_blogpost', 'price')


    models = {
        'author.blogpost': {
            'Meta': {'object_name': 'Blogpost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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