#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.
import typing
from typing import Callable, Optional, Union, Iterable

from azure.functions import AsgiMiddleware, WsgiMiddleware, Function
from azure.functions.decorators.core import DataType, \
    AuthLevel, Cardinality, AccessRights
from azure.functions.decorators.function_app import FunctionBuilder
from azure.functions.decorators.http import HttpMethod


class FunctionApp:
    """FunctionApp object used by worker function indexing model captures
       user defined functions and metadata.

       Ref: https://aka.ms/azure-function-ref
       """

    def __init__(self,
                 http_auth_level: Union[AuthLevel, str] = AuthLevel.FUNCTION,
                 **kwargs):
        """Constructor of :class:`FunctionApp` object.
        To integrate your asgi or wsgi application into python function,
        specify either of below variables as a keyword argument:
        `asgi_app` - the actual asgi application to integrate into python
        function.
        `wsgi_app` - the actual wsgi application to integrate into python
        function.

        :param http_auth_level: defaults to AuthLevel.FUNCTION, takes str or
        AuthLevel.
        :param kwargs: Extra arguments passed to :func:`__init__`.
        """

        pass

    @property
    def app_script_file(self) -> str:
        """Name of function app script file in which all the functions
         are defined. \n
         Script file defined here is for placeholder purpose, please refer to
         worker defined script file path as the single point of truth.

        :return: Script file name.
        """

        pass

    @property
    def auth_level(self) -> AuthLevel:
        """Authorization level of the function app. Will be applied to the http
         trigger functions which does not have authorization level specified.

        :return: Authorization level of the function app.
        """

        pass

    def get_functions(self) -> typing.List[Function]:
        """Get the function objects in the function app.

        :return: List of functions in the function app.
        """
        pass

    def _validate_type(self, func: Union[Callable, FunctionBuilder]) \
            -> FunctionBuilder:
        """Validate the type of the function object and return the created
        :class:`FunctionBuilder` object.


        :param func: Function object passed to
         :meth:`_configure_function_builder`
        :raises ValueError: Raise error when func param is neither
         :class:`Callable` nor :class:`FunctionBuilder`.
        :return: :class:`FunctionBuilder` object.
        """

        pass

    def _configure_function_builder(self, wrap) -> Callable:
        """Decorator function on user defined function to create and return
         :class:`FunctionBuilder` object from :class:`Callable` func.
        """

        pass

    def function_name(self, name: str) -> Callable:
        """Set name of the :class:`Function` object.

        :param name: Name of the function.
        :return: Decorator function.
        """

        pass

    def _add_http_app(self,
                      http_middleware: Union[
                          AsgiMiddleware, WsgiMiddleware]) -> None:
        """Add a Wsgi or Asgi app integrated http function.

        :param http_middleware: :class:`AsgiMiddleware` or
        :class:`WsgiMiddleware` instance.

        :return: None
        """

        pass

    def route(self,
              route: Optional[str] = None,
              trigger_arg_name: str = 'req',
              binding_arg_name: str = '$return',
              methods: Optional[
                  Union[Iterable[str], Iterable[HttpMethod]]] = None,
              auth_level: Optional[Union[AuthLevel, str]] = None,
              trigger_extra_fields: typing.Dict = {},
              binding_extra_fields: typing.Dict = {}
              ) -> Callable:
        """The route decorator adds :class:`HttpTrigger` and
        :class:`HttpOutput` binding to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining HttpTrigger
        and HttpOutput binding in the function.json which enables your
        function be triggered when http requests hit the specified route.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-http

        :param route: Route for the http endpoint, if None, it will be set
        to function name if present or user defined python function name.
        :param trigger_arg_name: Argument name for :class:`HttpRequest`,
        defaults to 'req'.
        :param binding_arg_name: Argument name for :class:`HttpResponse`,
        defaults to '$return'.
        :param methods: A tuple of the HTTP methods to which the function
        responds.
        :param auth_level: Determines what keys, if any, need to be present
        on the request in order to invoke the function.
        :return: Decorator function.
        :param trigger_extra_fields: Additional fields to include in trigger
        json. For example,
        >>> data_type='STRING' # 'dataType': 'STRING' in trigger json
        :param binding_extra_fields: Additional fields to include in binding
        json. For example,
        >>> data_type='STRING' # 'dataType': 'STRING' in binding json
        """

        pass

    def schedule(self,
                 arg_name: str,
                 schedule: str,
                 run_on_startup: Optional[bool] = None,
                 use_monitor: Optional[bool] = None,
                 data_type: Optional[Union[DataType, str]] = None,
                 **kwargs) -> Callable:
        """The schedule decorator adds :class:`TimerTrigger` to the
        :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining TimerTrigger
        in the function.json which enables your function be triggered on the
        specified schedule.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-timer

        :param arg_name: The name of the variable that represents the
        :class:`TimerRequest` object in function code.
        :param schedule: A string representing a CRON expression that will
        be used to schedule a function to run.
        :param run_on_startup: If true, the function is invoked when the
        runtime starts.
        :param use_monitor: Set to true or false to indicate whether the
        schedule should be monitored.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def service_bus_queue_trigger(
            self,
            arg_name: str,
            connection: str,
            queue_name: str,
            data_type: Optional[Union[DataType, str]] = None,
            access_rights: Optional[Union[AccessRights, str]] = None,
            is_sessions_enabled: Optional[bool] = None,
            cardinality: Optional[Union[Cardinality, str]] = None,
            **kwargs) -> Callable:
        """The on_service_bus_queue_change decorator adds
        :class:`ServiceBusQueueTrigger` to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining ServiceBusQueueTrigger
        in the function.json which enables your function be triggered when
        new message(s) are sent to the service bus queue.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-service-bus

        :param arg_name: The name of the variable that represents the
        :class:`ServiceBusMessage` object in function code.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Service Bus.
        :param queue_name: Name of the queue to monitor.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :param access_rights: Access rights for the connection string.
        :param is_sessions_enabled: True if connecting to a session-aware
        queue or subscription.
        :param cardinality: Set to many in order to enable batching.
        :return: Decorator function.
        """

        pass

    def write_service_bus_queue(self,
                                arg_name: str,
                                connection: str,
                                queue_name: str,
                                data_type: Optional[
                                    Union[DataType, str]] = None,
                                access_rights: Optional[Union[
                                    AccessRights, str]] = None,
                                **kwargs) -> \
            Callable:
        """The write_service_bus_queue decorator adds
        :class:`ServiceBusQueueOutput` to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining ServiceBusQueueOutput
        in the function.json which enables function to write message(s) to
        the service bus queue.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-service-bus

        :param arg_name: The name of the variable that represents service
        bus queue output object in function code.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Service Bus.
        :param queue_name: Name of the queue to monitor.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :param access_rights: Access rights for the connection string.
        :return: Decorator function.
        """

        pass

    def service_bus_topic_trigger(
            self,
            arg_name: str,
            connection: str,
            topic_name: str,
            subscription_name: str,
            data_type: Optional[Union[DataType, str]] = None,
            access_rights: Optional[Union[AccessRights, str]] = None,
            is_sessions_enabled: Optional[bool] = None,
            cardinality: Optional[Union[Cardinality, str]] = None,
            **kwargs) -> Callable:
        """The on_service_bus_topic_change decorator adds
        :class:`ServiceBusTopicTrigger` to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining ServiceBusTopicTrigger
        in the function.json which enables function to be triggered when new
        message(s) are sent to the service bus topic.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-service-bus

        :param arg_name: The name of the variable that represents the
        :class:`ServiceBusMessage` object in function code.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Service Bus.
        :param topic_name: Name of the topic to monitor.
        :param subscription_name: Name of the subscription to monitor.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :param access_rights: Access rights for the connection string.
        :param is_sessions_enabled: True if connecting to a session-aware
        queue or subscription.
        :param cardinality: Set to many in order to enable batching.
        :return: Decorator function.
        """

        pass

    def write_service_bus_topic(self,
                                arg_name: str,
                                connection: str,
                                topic_name: str,
                                subscription_name: Optional[str] = None,
                                data_type: Optional[
                                    Union[DataType, str]] = None,
                                access_rights: Optional[Union[
                                    AccessRights, str]] = None,
                                **kwargs) -> \
            Callable:
        """The write_service_bus_topic decorator adds
        :class:`ServiceBusTopicOutput` to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining ServiceBusTopicOutput
        in the function.json which enables function to write message(s) to
        the service bus topic.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-service-bus

        :param arg_name: The name of the variable that represents service
        bus topic output object in function code.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Service Bus.
        :param topic_name: Name of the topic to monitor.
        :param subscription_name: Name of the subscription to monitor.
        :param data_type: Defines how Functions runtime should treat the
        parameter value, defaults to DataType.UNDEFINED.
        :param access_rights: Access rights for the connection string.
        :return: Decorator function.
        """

        pass

    def queue_trigger(self,
                      arg_name: str,
                      queue_name: str,
                      connection: str,
                      data_type: Optional[DataType] = None,
                      **kwargs) -> Callable:
        """The queue_trigger decorator adds :class:`QueueTrigger` to the
        :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining QueueTrigger
        in the function.json which enables function to be triggered when new
        message(s) are sent to the storage queue.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-queue

        :param arg_name: The name of the variable that represents the
        :class:`QueueMessage` object in function code.
        :param queue_name: The name of the queue to poll.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Azure Queues.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def write_queue(self,
                    arg_name: str,
                    queue_name: str,
                    connection: str,
                    data_type: Optional[DataType] = None,
                    **kwargs) -> Callable:
        """The write_queue decorator adds :class:`QueueOutput` to the
        :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining QueueOutput
        in the function.json which enables function to write message(s) to
        the storage queue.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-queue

        :param arg_name: The name of the variable that represents storage
        queue output object in function code.
        :param queue_name: The name of the queue to poll.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Azure Queues.
        :param data_type: Defines how Functions runtime should treat the
         parameter value.
        :return: Decorator function.
        """

        pass

    def event_hub_message_trigger(self,
                                  arg_name: str,
                                  connection: str,
                                  event_hub_name: str,
                                  data_type: Optional[
                                      Union[DataType, str]] = None,
                                  cardinality: Optional[
                                      Union[Cardinality, str]] = None,
                                  consumer_group: Optional[
                                      str] = None,
                                  **kwargs) -> Callable:
        """The event_hub_message_trigger decorator adds
        :class:`EventHubTrigger`
        to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining EventHubTrigger
        in the function.json which enables function to be triggered when new
        message(s) are sent to the event hub.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-event-hubs

        :param arg_name: The name of the variable that represents
        :class:`EventHubEvent` object in function code.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Event Hubs.
        :param event_hub_name: The name of the event hub.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :param cardinality: Set to many in order to enable batching.
        :param consumer_group: An optional property that sets the consumer
        group used to subscribe to events in the hub.
        :return: Decorator function.
        """

        pass

    def write_event_hub_message(self,
                                arg_name: str,
                                connection: str,
                                event_hub_name: str,
                                data_type: Optional[
                                    Union[DataType, str]] = None,
                                **kwargs) -> \
            Callable:
        """The write_event_hub_message decorator adds
        :class:`EventHubOutput` to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining EventHubOutput
        in the function.json which enables function to write message(s) to
        the event hub.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-event-hubs

        :param arg_name: The name of the variable that represents event hub
        output object in function code.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Event Hub.
        :param event_hub_name: The name of the event hub.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def cosmos_db_trigger(self,
                          arg_name: str,
                          database_name: str,
                          collection_name: str,
                          connection_string_setting: str,
                          lease_collection_name: Optional[str] = None,
                          lease_connection_string_setting: Optional[
                              str] = None,
                          lease_database_name: Optional[str] = None,
                          create_lease_collection_if_not_exists: Optional[
                              bool] = None,
                          leases_collection_throughput: Optional[int] = None,
                          lease_collection_prefix: Optional[str] = None,
                          checkpoint_interval: Optional[int] = None,
                          checkpoint_document_count: Optional[int] = None,
                          feed_poll_delay: Optional[int] = None,
                          lease_renew_interval: Optional[int] = None,
                          lease_acquire_interval: Optional[int] = None,
                          lease_expiration_interval: Optional[int] = None,
                          max_items_per_invocation: Optional[int] = None,
                          start_from_beginning: Optional[bool] = None,
                          preferred_locations: Optional[str] = None,
                          data_type: Optional[
                              Union[DataType, str]] = None,
                          **kwargs) -> \
            Callable:
        """The cosmos_db_trigger decorator adds :class:`CosmosDBTrigger`
        to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining CosmosDBTrigger
        in the function.json which enables function to be triggered when
        CosmosDB data is changed.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-cosmosdb-v2

        :param arg_name: The name of the variable that represents
        :class:`DocumentList` object in function code.
        :param database_name: The name of the Azure Cosmos DB database with
        the collection being monitored.
        :param collection_name: The name of the collection being monitored.
        :param connection_string_setting: The name of an app setting or
        setting collection that specifies how to connect to the Azure Cosmos
        DB account being monitored.
        :param lease_collection_name: The name of the collection used to
        store leases.
        :param lease_connection_string_setting: The name of an app setting
        or setting collection that specifies how to connect to the Azure
        Cosmos DB account that holds the lease collection.
        :param lease_database_name: The name of the database that holds the
        collection used to store leases.
        :param create_lease_collection_if_not_exists: When set to true,
        the leases collection is automatically created when it doesn't
        already exist.
        :param leases_collection_throughput: Defines the number of Request
        Units to assign when the leases collection is created.
        :param lease_collection_prefix: When set, the value is added as a
        prefix to the leases created in the Lease collection for this
        Function.
        :param checkpoint_interval: When set, it defines, in milliseconds,
        the interval between lease checkpoints. Default is always after a
        Function call.
        :param checkpoint_document_count: Customizes the amount of documents
        between lease checkpoints. Default is always after a Function call.
        :param feed_poll_delay: The time (in milliseconds) for the delay
        between polling a partition for new changes on the feed, after all
        current changes are drained.
        :param lease_renew_interval: When set, it defines, in milliseconds,
        the renew interval for all leases for partitions currently held by
        an instance.
        :param lease_acquire_interval: When set, it defines,
        in milliseconds, the interval to kick off a task to compute if
        partitions are distributed evenly among known host instances.
        :param lease_expiration_interval: When set, it defines,
        in milliseconds, the interval for which the lease is taken on a
        lease representing a partition.
        :param max_items_per_invocation: When set, this property sets the
        maximum number of items received per Function call.
        :param start_from_beginning: This option tells the Trigger to read
        changes from the beginning of the collection's change history
        instead of starting at the current time.
        :param preferred_locations: Defines preferred locations (regions)
        for geo-replicated database accounts in the Azure Cosmos DB service.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def write_cosmos_db_documents(self,
                                  arg_name: str,
                                  database_name: str,
                                  collection_name: str,
                                  connection_string_setting: str,
                                  create_if_not_exists: Optional[bool] = None,
                                  partition_key: Optional[str] = None,
                                  collection_throughput: Optional[int] = None,
                                  use_multiple_write_locations: Optional[
                                      bool] = None,
                                  preferred_locations: Optional[str] = None,
                                  data_type: Optional[
                                      Union[DataType, str]] = None,
                                  **kwargs) \
            -> Callable:
        """The write_cosmos_db_documents decorator adds
        :class:`CosmosDBOutput` to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining CosmosDBOutput
        in the function.json which enables function to write to the CosmosDB.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-cosmosdb-v2

        :param arg_name: The name of the variable that represents CosmosDB
        output object in function code.
        :param database_name: The name of the Azure Cosmos DB database with
        the collection being monitored.
        :param collection_name: The name of the collection being monitored.
        :param connection_string_setting: The name of an app setting or
        setting collection that specifies how to connect to the Azure Cosmos
        DB account being monitored.
        :param create_if_not_exists: A boolean value to indicate whether the
        collection is created when it doesn't exist.
        :param partition_key: When CreateIfNotExists is true, it defines the
        partition key path for the created collection.
        :param collection_throughput: When CreateIfNotExists is true,
        it defines the throughput of the created collection.
        :param use_multiple_write_locations: When set to true along with
        PreferredLocations, it can leverage multi-region writes in the Azure
        Cosmos DB service.
        :param preferred_locations: Defines preferred locations (regions)
        for geo-replicated database accounts in the Azure Cosmos DB service.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def read_cosmos_db_documents(self,
                                 arg_name: str,
                                 database_name: str,
                                 collection_name: str,
                                 connection_string_setting: str,
                                 id: Optional[str] = None,
                                 sql_query: Optional[str] = None,
                                 partition_key: Optional[str] = None,
                                 data_type: Optional[
                                     Union[DataType, str]] = None,
                                 **kwargs) \
            -> Callable:
        """The read_cosmos_db_documents decorator adds
        :class:`CosmosDBInput` to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining CosmosDBInput
        in the function.json which enables function to read from CosmosDB.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-cosmosdb-v2

        :param arg_name: The name of the variable that represents
        :class:`DocumentList` input object in function code.
        :param database_name: The database containing the document.
        :param collection_name: The name of the collection that contains the
        document.
        :param connection_string_setting: The name of the app setting
        containing your Azure Cosmos DB connection string.
        :param id: The ID of the document to retrieve.
        :param sql_query: An Azure Cosmos DB SQL query used for retrieving
        multiple documents.
        :param partition_key: Specifies the partition key value for the
        lookup.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def blob_trigger(self,
                     arg_name: str,
                     path: str,
                     connection: str,
                     data_type: Optional[DataType] = None,
                     **kwargs) -> Callable:
        """
        The blob_change_trigger decorator adds :class:`BlobTrigger` to the
        :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining BlobTrigger
        in the function.json which enables function to be triggered when new
        message(s) are sent to the storage blobs.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-storage-blob

        :param arg_name: The name of the variable that represents the
        :class:`InputStream` object in function code.
        :param path: The path to the blob.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Azure Blobs.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def read_blob(self,
                  arg_name: str,
                  path: str,
                  connection: str,
                  data_type: Optional[DataType] = None,
                  **kwargs) -> Callable:

        """
        The read_blob decorator adds :class:`BlobInput` to the
        :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining BlobInput
        in the function.json which enables function to write message(s) to
        the storage blobs.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-storage-blob

        :param arg_name: The name of the variable that represents the blob in
         function code.
        :param path: The path to the blob.
        :param connection: The name of an app setting or setting collection
        that specifies how to connect to Azure Blobs.
        :param data_type: Defines how Functions runtime should treat the
         parameter value.
        :return: Decorator function.
        """

        pass

    def write_blob(self,
                   arg_name: str,
                   path: str,
                   connection: str,
                   data_type: Optional[DataType] = None,
                   **kwargs) -> Callable:

        """
        The write_blob decorator adds :class:`BlobOutput` to the
        :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining BlobOutput
        in the function.json which enables function to write message(s) to
        the storage blobs.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-storage-blob

        :param arg_name: The name of the variable that represents the blob in
         function code.
        :param path: The path to the blob.
        :param connection: The name of an app setting or setting collection
         that specifies how to connect to Azure Blobs.
        :param data_type: Defines how Functions runtime should treat the
         parameter value.
        :return: Decorator function.
        """

        pass

    def generic_input_binding(self,
                              arg_name: str,
                              type: str,
                              data_type: Optional[Union[DataType, str]] = None,
                              **kwargs
                              ) -> Callable:
        """
        The generic_input_binding decorator adds :class:`GenericInputBinding`
        to the :class:`FunctionBuilder` object for building :class:`Function`
        object used in worker function indexing model.
        This is equivalent to defining a generic input binding in the
        function.json which enables function to read data from a
        custom defined input source.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-custom

        :param arg_name: The name of input parameter in the function code.
        :param type: The type of binding.
        :param data_type: Defines how Functions runtime should treat the
         parameter value.
        :param kwargs: Keyword arguments for specifying additional binding
        fields to include in the binding json.

        :return: Decorator function.
        """

        pass

    def generic_output_binding(self,
                               arg_name: str,
                               type: str,
                               data_type: Optional[
                                   Union[DataType, str]] = None,
                               **kwargs
                               ) -> Callable:
        """
        The generic_output_binding decorator adds :class:`GenericOutputBinding`
        to the :class:`FunctionBuilder` object for building :class:`Function`
        object used in worker function indexing model.
        This is equivalent to defining a generic output binding in the
        function.json which enables function to write data from a
        custom defined output source.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-custom

        :param arg_name: The name of output parameter in the function code.
        :param type: The type of binding.
        :param data_type: Defines how Functions runtime should treat the
         parameter value.
        :param kwargs: Keyword arguments for specifying additional binding
        fields to include in the binding json.

        :return: Decorator function.
        """

        pass

    def generic_trigger(self,
                        arg_name: str,
                        type: str,
                        data_type: Optional[Union[DataType, str]] = None,
                        **kwargs
                        ) -> Callable:
        """
        The generic_trigger decorator adds :class:`GenericTrigger`
        to the :class:`FunctionBuilder` object for building :class:`Function`
        object used in worker function indexing model.
        This is equivalent to defining a generic trigger in the
        function.json which triggers function to execute when generic trigger
        events are received by host.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/azure-function-binding-custom

        :param arg_name: The name of trigger parameter in the function code.
        :param type: The type of binding.
        :param data_type: Defines how Functions runtime should treat the
         parameter value.
        :param kwargs: Keyword arguments for specifying additional binding
        fields to include in the binding json.

        :return: Decorator function.
        """

        pass

    def event_grid_trigger(self,
                           arg_name: str,
                           data_type: Optional[
                               Union[DataType, str]] = None,
                           **kwargs) -> Callable:
        """
        The event_grid_trigger decorator adds
        :class:`EventGridTrigger`
        to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining event grid trigger
        in the function.json which enables function to be triggered to
        respond to an event sent to an event grid topic.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/eventgridtrigger

        :param arg_name: the variable name used in function code for the
         parameter that receives the event data.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :return: Decorator function.
        """

        pass

    def write_event_grid(self,
                         arg_name: str,
                         topic_endpoint_uri: str,
                         topic_key_setting: str,
                         data_type: Optional[
                             Union[DataType, str]] = None,
                         **kwargs) -> Callable:
        """
        The write_event_grid decorator adds
        :class:`EventGridOutput`
        to the :class:`FunctionBuilder` object
        for building :class:`Function` object used in worker function
        indexing model. This is equivalent to defining output binding
        in the function.json which enables function to
        write events to a custom topic.
        All optional fields will be given default value by function host when
        they are parsed by function host.

        Ref: https://aka.ms/eventgridtrigger

        :param arg_name: The variable name used in function code that
        represents the event.
        :param data_type: Defines how Functions runtime should treat the
        parameter value.
        :param topic_endpoint_uri: 	The name of an app setting that
        contains the URI for the custom topic.
        :param topic_key_setting: The name of an app setting that
        contains an access key for the custom topic.
        :return: Decorator function.
        """

        pass

