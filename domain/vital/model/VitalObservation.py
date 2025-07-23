#!/usr/bin/python
#-*- coding: utf-8 -*-
from extensions import db
from datetime import datetime

class VitalObservation(db.Model):
    __tablename__ = 'vital_observations'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    observed_at = db.Column(db.DateTime, default=datetime.utcnow)
    document_id = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<VitalObservation {self.id} - {self.title}>'

    def attach_to_document(self, document):
        self.document_id = document.id