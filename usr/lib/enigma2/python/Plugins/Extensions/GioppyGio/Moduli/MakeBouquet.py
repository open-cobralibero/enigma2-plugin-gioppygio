import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
