# Socket-Protocol

Simple socket based protocol

### Request Format:

```json
{
  "action": "<string>",
  "service": "<string>",
  "params": "<object>",
  "content": "<list | object>"
}
```

### Response Format:

```json
{
  "status": "<string>",
  "content": "<list | object>"
}
```

#### Error codes:

- S0: OK
- S1: CREATED
- S2: UPDATED
- S3: DELETED
- CE0: BAD REQUEST
- CE1: PERMISSION DENIED
- CE2: NOT FOUND
- SE0: INTERNAL SERVER ERROR
- SE1: NOT AVAILABLE
