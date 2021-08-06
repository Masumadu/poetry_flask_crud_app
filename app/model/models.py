from ..app import db, ma
from flask_marshmallow import fields
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema


class BillableHourModel(db.Model):
    __tablename__ = 'billing_hours'
    id = db.Column('Employee ID', db.Integer, primary_key=True)
    billable_rate = db.Column('Billable Rare (per hour)', db.Integer, nullable=False)
    company = db.Column('Company', db.String(60), primary_key=True)
    date = db.Column('Date', db.Date())
    start_time = db.Column('Start Time', db.Time())
    end_time = db.Column('End Time', db.Time())

    def __init__(self, employee_id, billable_rate, company, date, start_time, end_time):
        self.id = employee_id
        self.billable_rate = billable_rate
        self.company = company
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"<Company {self.company}>"


class BillableHourSchema(ma.Schema):
    class Meta:
        fields = ('id', 'company', 'billable_rate')

# class BillableHourSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = BillableHourModel
#
#     id = ma.auto_field()
#     company = ma.auto_field()
#     billable_rate = ma.auto_field()


# using marshmallow-sqlalchemy to serialize data
# class BillableHourSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = BillableHourModel
#         load_instance = True

# using flask-marshmallow to serialize data
# 1.
# class BillableHourSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = BillableHourModel
#
#     id = ma.auto_field()
#     company = ma.auto_field()
#     billable_rate = ma.auto_field()
# 2.
# class BillableHourSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'company')
