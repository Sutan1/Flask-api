from marshmallow import Schema, fields

# Item Plain
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

# Store Plain
class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

# Tag Plain
class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

    ### Item
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema), dump_only=True)

    ### Item Update
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

    ### Store
class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

    ### Tag
class TagSchema(PlainTagSchema):
    id = fields.Int(load_only = True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema), dump_only=True)

### Tags and Items ###
class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)

# User
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)