# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DrinkOrder.fulfilled'
        db.add_column('drinks_drinkorder', 'fulfilled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'DrinkOrder.placed'
        db.add_column('drinks_drinkorder', 'placed',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 12, 13, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DrinkOrder.fulfilled'
        db.delete_column('drinks_drinkorder', 'fulfilled')

        # Deleting field 'DrinkOrder.placed'
        db.delete_column('drinks_drinkorder', 'placed')


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
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'placed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['drinks']