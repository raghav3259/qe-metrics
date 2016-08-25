xunitMapping = {"mappings": {
    "testjob": {
        "properties": {
            "change_set": {
                "type": "string",
                "index": "not_analyzed"
            },
            "culprits": {
                "type": "string",
                "index": "not_analyzed"
            },
            "duration": {
                "type": "long"
            },
            "estimatedDuration": {
                "type": "long"
            },
            "id": {
                "type": "long"
            },
            "name": {
                "type": "string"
            },
            "result": {
                "type": "string"
            },
            "time": {
                "type": "date",
                "format": "dateOptionalTime"
            }
        }
    },
    "testsuite": {
        "_parent": {
            "type": "testjob"
        }
    },
    "testcase": {
        "_parent": {
            "type": "testsuite"
        }
    }
}
}
