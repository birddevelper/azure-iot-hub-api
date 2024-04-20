def _ensure_quoted(etag):
    if not isinstance(etag, str) or (len(etag) > 1 and etag[0] == '"' and etag[-1] == '"'):
        return etag
    return '"' + etag + '"'