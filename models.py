

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import sqlalchemy as sa
import datetime
from sqlalchemy.dialects import postgresql
import pytest


Base = declarative_base()
metadata = Base.metadata




class Plan(Base):
    __tablename__ = "plan"
    id = Column("id",Integer,primary_key=True)
    plan_name = Column("plan_name",String)
    plan_type = Column("plan_type",String)
    percentage = Column("percentage",String)
    fix_month = Column("fix_month",String,nullable=True)
    notes = Column("notes",String,nullable=True)
    created_at = Column('created_at',postgresql.TIMESTAMP())
    
    
    def __init__(self,id,plan_name,plan_type,percentage,fix_month,notes,created_at):
        self.id = id
        self.plan_name = plan_name
        self.plan_type = plan_type
        self.percentage = percentage
        self.fix_month = fix_month
        self.notes = notes
        self.created_at = created_at
    
    def __repr__(self):
        return f"({self.id} {self.plan_name}  {self.plan_type} {self.percentage} {self.fix_month} {self.notes} {self.created_at})"
    
    
class Investors(Base):
    __tablename__ = "investors"
    id = Column("id",Integer,primary_key=True)
    investor_name = Column("investor_name",String)
    mobile_no = Column("mobile_no",String)
    email = Column("email",String)
    city_name = Column("city_name",String)
    unique_code = Column("unique_code",String)
    account_number = Column("account_number",String)
    ifsc_code = Column("ifsc_code",String)
    created_at = Column('created_at',postgresql.TIMESTAMP())
    

    def __init__(self,id,investor_name,mobile_no,email,city_name,unique_code,account_number,ifsc_code,created_at):
        self.id = id
        self.investor_name = investor_name
        self.mobile_no = mobile_no
        self.email = email
        self.city_name = city_name
        self.unique_code = unique_code
        self.account_number = account_number
        self.ifsc_code = ifsc_code
        self.created_at = created_at
        
        
    def __repr__(self):
        return f"({self.id} {self.investor_name}  {self.mobile_no} {self.email} {self.city_name} {self.unique_code}  {self.account_number} {self.ifsc_code} {self.created_at})"
    
    
    
class Collection(Base):
    __tablename__ = "collection"
    
    id = Column("id",Integer,primary_key=True)
    investor_name = Column(Integer , ForeignKey("investors.id"))
    plan_name = Column(Integer ,  ForeignKey("plan.id"))
    amount = Column('amount',Integer)
    created_at = Column('created_at',postgresql.TIMESTAMP())

    
    def __init__(self,id,investor_name,plan_name,amount,created_at):
        self.id = id
        self.investor_name = investor_name
        self.plan_name = plan_name
        self.amount = amount
        self.created_at = created_at
        
    def __repr__(self):
        return f"({self.id} {self.investor_name}  {self.plan_name} {self.amount} {self.created_at})"
    
    
class Withdrawal(Base):
    __tablename__ = "withdrwal"
    
    id = Column("id",Integer,primary_key=True)
    investor_name = Column(Integer , ForeignKey("investors.id"))
    plan_name = Column(Integer ,  ForeignKey("plan.id"))
    amount = Column('amount',Integer)
    created_at = Column('created_at',postgresql.TIMESTAMP())
    
        
    def __init__(self,id,investor_name,plan_name,amount,created_at):
        self.id = id
        self.investor_name = investor_name
        self.plan_name = plan_name
        self.amount = amount
        self.created_at = created_at
        
    def __repr__(self):
        return f"({self.id} {self.investor_name}  {self.plan_name} {self.amount} {self.created_at})"
    
    
class Profile(Base):
    __tablename__ = "investor_profile"
    
    id = Column("id",Integer,primary_key=True)
    investor_name = Column(Integer , ForeignKey("investors.id"))
    plan_name = Column(Integer ,  ForeignKey("plan.id"))
    total_amount = Column('total_amount',Integer)
    created_at = Column('created_at',postgresql.TIMESTAMP())
    
    
    def __init__(self,id,investor_name,plan_name,total_amount,created_at):
        self.id = id
        self.investor_name = investor_name
        self.plan_name = plan_name
        self.total_amount = total_amount
        self.created_at = created_at
        
    def __repr__(self):
        return f"({self.id} {self.investor_name}  {self.plan_name} {self.total_amount} {self.created_at})"
    


engine = create_engine('{Add database url}',echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# plan details
# plan1 = Plan(1,'Gold','percentage','4',"","4 month",datetime.datetime.now())
# # session.add(plan1)

# plan2 = Plan(2,"Silver","fix","3","36","36 month 3%",datetime.datetime.now())
# # session.add(plan2)



# # party details

# party1 = Investors(1,"Suhani Timbadiya","8866349316","suhanitimbadiya@gmail.com","Ahemedabad","25.25","123456789123","BOBCD0S",datetime.datetime.now())
# party2 = Investors(2,"Kishan Patel","8866349316","kishan286@gmail.com","Surat","74.25","98745632145","PLAS345",datetime.datetime.now())
# # session.add(party1)
# # session.add(party2)

# # Collection details

# collection1 = Collection(1,party1.id,plan1.id,1000,datetime.datetime.now())
# collection2 = Collection(2,party2.id,plan2.id,5000,datetime.datetime.now())

# # session.add(collection1)
# # session.add(collection2)

# # # Withdrawal details
# withdrawal1 = Withdrawal(1,party1.id,plan1.id,500,datetime.datetime.now())
# withdrawal2 = Withdrawal(2,party2.id,plan2.id,100,datetime.datetime.now())

# # session.add(withdrawal1)
# # session.add(withdrawal2)


# # # Profile details
# profile1 = Profile(1,party1.id,plan1.id,collection1.amount-withdrawal1.amount,datetime.datetime.now())
# profile2 = Profile(2,party2.id,plan2.id,collection2.amount-withdrawal2.amount,datetime.datetime.now())
# session.add(profile1)
# session.add(profile2)

# result = session.query(Profile)
# for x in result:
#     print(x)
    
session.commit()


