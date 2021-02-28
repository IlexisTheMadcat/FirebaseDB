# FirebaseDB 0.5
Create a simple CRUD operations helper for Google Firebase Realtime Databases. \
Currently incompatible with Cloud Firestore. \

**Initiate with these arguments:** \
`databaseURL` - Works with Realtime Databases. Open it and copy its link. \
`fp_accountkey_json` - Fetch this file from the Project settings: \
    Service Accounts > Firebase Admin SDK > Python > Generate new private key. \
`app_name` - Initialize the app with this name. *Note that no two instances of this class can have the same name.* \
`dbroot_path` - Choose the path of the database dict to start from. This is the destination key whose value will be overwritten. \

**Returns:** \
ー Attr:`FirebaseDB.project_id` - The project ID that this class is operating on. Useful to check if 2 instances are running on the same project. \
ー Attr: `FirebaseDB.instance_name` - Returns `app_name` from `__init__` for later use. Again, no two instances with the same name can co-exist. \
ー Attr: `FirebaseDB.refer` - The Reference object that this class operates on. You can perform manual operations with it if you know how to use the SDK. \
ー Attr: `FirebaseDB._dbroot_path` - Returns `dbroot_path` from `__init__` for later use. Used to stay persistant with the root key. \

**Reading (HTTP GET):** \
ー Func: `FirebaseDB.get(key, default=None)` - Equal to dict().get(); Returns the requested value. If `value` is not found, returns `default`. \
ー Func: `FirebaseDB.keys()` - Equal to dict().keys(); Returns list of keys at the root. \
ー Func: `FirebaseDB.values()` - Equal to dict().values(); Returns list of values at the root. \
ー Func: `FirebaseDB.items()` - Equal to dict().items(); Returns list of keys at the root. \
ー Func: `FirebaseDB.copy()` - Equal to dict().copy(); Returns an exact copy of the database. \

**Writing (HTTP GET>WRITE>POST):** \
ー Func: `FirebaseDB.update(json)` - Equal to dict().update(); Returns the class instance. \
ー Func: `FirebaseDB.clear()` - Equal to dict().clear(); Returns the class instance. \
ー Func: `FirebaseDB.pop(key)` - Equal to dict().pop(); Returns the deleted key's value. \
ー Func: `FirebaseDB.popitem()` - Equal to dict().popitem(); Returns the last (key, value) added. \
ー Func: `FirebaseDB.overwrite(json)` - Additional method to completely overwrite the database with `json`. 
    If `json` is omitted, alias for `FirebaseDB.clear()`.
    Functionally identical to `FirebaseDB.clear().update(json)`. \

**Note**: \
While a dictionary can have nested values, editing values in nested levels will **NOT** 
    send updates to the database and you may lose your data. To counter this, `.copy()` the database and 
    make any pythonic change to the returned dictionary. Then, call `.overwrite(json)`, where `json` is your
    updated dictionary.
