smsified
========

An easy-to-use Python wrapper for [SMSified](https://smsified.com/).


Installation
------------

```
pip install smsified
```


Usage
-----

Make sure to set the following environment variables to reduce
the preliminary, boilerplate setup.

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

# Send a message to 415-456-7890.
>>> s.send('Hey, you!', '415-456-7890')

# And, we can switch it up at any time.
>>> s.number('415-456-7890')
>>> s.send('ohai', '415-123-4567')
```
