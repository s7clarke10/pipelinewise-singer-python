from __future__ import annotations

from singer import utils
from singer.bookmarks import (
    clear_bookmark,
    clear_offset,
    get_bookmark,
    get_currently_syncing,
    get_offset,
    reset_stream,
    set_currently_syncing,
    set_offset,
    write_bookmark,
)
from singer.catalog import Catalog, CatalogEntry
from singer.logger import get_logger
from singer.messages import (
    ActivateVersionMessage,
    BatchMessage,
    Message,
    RecordMessage,
    SchemaMessage,
    StateMessage,
    format_message,
    parse_message,
    write_batch,
    write_message,
    write_record,
    write_records,
    write_schema,
    write_state,
    write_version,
)
from singer.metrics import (
    Counter,
    Timer,
    http_request_timer,
    job_timer,
    record_counter,
)
from singer.schema import Schema
from singer.transform import (
    NO_INTEGER_DATETIME_PARSING,
    UNIX_MILLISECONDS_INTEGER_DATETIME_PARSING,
    UNIX_SECONDS_INTEGER_DATETIME_PARSING,
    Transformer,
    _transform_datetime,
    resolve_schema_references,
    transform,
)
from singer.utils import (
    chunk,
    load_json,
    parse_args,
    ratelimit,
    should_sync_field,
    strftime,
    strptime,
    update_state,
)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
