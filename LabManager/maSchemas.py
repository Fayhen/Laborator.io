from marshmallow import fields
# from marshmallow_sqlalchemy import ModelSchema
from LabManager import ma
from LabManager.dbModels import PersonType, Gender, Person, User, FrequencyEvent, Inventory, Lendings, TechnicalIssues, Notices, FieldEvent


# class SmartNested(fields.Nested):
#     def serialize(self, attr, obj, accessor=None):
#         if attr not in obj.__dict__:
#             return {"id": int(getattr(obj, attr + "_id"))}
#         return super(SmartNested, self).serialize(attr, obj, accessor)


# Marshmellow schema definitions
class TypeSchema(ma.ModelSchema):
    class Meta:
        model = PersonType


class GenreSchema(ma.ModelSchema):
    class Meta:
        model = Gender


class PersonSchema(ma.ModelSchema):
    # person_type = SmartNested(TypeSchema)
    # gender = SmartNested(GenreSchema)
    class Meta:
        model = Person


class UserSchema(ma.ModelSchema):
    # person = SmartNested(PersonSchema)
    class Meta:
        model = User


class FrequencySchema(ma.ModelSchema):
    # person = SmartNested(PersonSchema)
    class Meta:
        model = FrequencyEvent


class InventorySchema(ma.ModelSchema):
    class Meta:
        model = Inventory


class LendingSchema(ma.ModelSchema):
    # equipment = SmartNested(InventorySchema)
    class Meta:
        model = Lendings


class IssueSchema(ma.ModelSchema):
    # equipment = SmartNested(InventorySchema)
    class Meta:
        model = TechnicalIssues



class NoticeSchema(ma.ModelSchema):
    # user = SmartNested(UserSchema)
    class Meta:
        model = Notices



class FieldSchema(ma.ModelSchema):

    class Meta:
        model = FieldEvent


# Marshmallow schema inits
type_schema = TypeSchema(strict=True)
genre_schema = GenreSchema(strict=True)
person_schema = PersonSchema(strict=True)
persons_schema = PersonSchema(many=True, strict=True)
user_schema = UserSchema(strict=True)
frequency_schema = FrequencySchema(strict=True)
equipment_schema = InventorySchema(strict=True)
equipments_schema = InventorySchema(many=True, strict=True)
lending_schema = LendingSchema(strict=True)
lendings_schema = LendingSchema(many=True, strict=True)
issue_schema = IssueSchema(strict=True)
issues_schema = IssueSchema(many=True, strict=True)
notice_schema = NoticeSchema(strict=True)
notices_schema = NoticeSchema(many=True, strict=True)
field_schema = FieldSchema(strict=True)
fields_schema = FieldSchema(many=True, strict=True)