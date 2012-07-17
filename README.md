smsified
========

An easy-to-use Python wrapper for SMSified.


Installation
------------

```
pip install pets
```


Usage
-----

Make sure to set the following environment variables.

```
export SMS_USER=smsified_username
export SMS_PASS=smsified_password
```

You can then import the `smsified` Python library.

```python
>>> import smsified as s

# Oops, we forgot to set our username and password. No worries.
>>> s.auth('smsified_username', 'smsified_password')

# Now, set your current SMSified number.
>>> s.number('415-123-4567')

# Send a message.
>>> s.send('Hey, you!', '415-456-7890')

# We can switch it up at any time.
>>> s.number('415-456-7890')
>>> s.send('ohai', '415-123-4567')
```
