# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DrinkOrder'
        db.create_table('drinks_drinkorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drink', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drinks.Drink'])),
            ('person', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('drinks', ['DrinkOrder'])


    def backwards(self, orm):
        # Deleting model 'DrinkOrder'
        db.delete_table('drinks_drinkorder')


    models = {
        'drinks.drink': {
            'Meta': {'object_name': 'Drink'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'drinks.drinkorder': {
            'Meta': {'object_name': 'DrinkOrder'},
            'drink': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['drinks.Drink']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['drinks']