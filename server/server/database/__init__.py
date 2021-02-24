from __future__ import annotations



# def auto_reconnect(func: Callable) -> Callable:
#     @wraps(func)
#     async def retry(*args: Any, **kwargs: Any) -> Any:
#         """Retry given method for multiple times in increasing intervals."""
#         max_attempts = 4
#         timeout = 5
#
#         for attempt in range(1, max_attempts + 1):
#             try:
#                 return await func(*args, **kwargs)
#             except (ClientConnectionError, ConnectionAbortedError) as error:
#                 if attempt == max_attempts:
#                     logger.error(
#                         f"Connection to database failed after {attempt} " "tries"
#                     )
#                     raise error
#                 logger.error(
#                     f"Connection not successful, trying to reconnect."
#                     f"Reconnection attempt number {attempt}, waiting "
#                     f" for {timeout} seconds."
#                 )
#                 await asyncio.sleep(timeout)
#                 timeout *= 2
#                 continue
#
#     return retry
