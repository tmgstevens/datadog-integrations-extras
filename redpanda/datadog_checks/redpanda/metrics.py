# metrics namespaced under 'redpanda'
VECTORIZED_APPLICATION = {
    'redpanda_application_uptime_seconds_total': 'application.uptime',
    'redpanda_application_build': 'application.build',
}

VECTORIZED_CONTROLLER = {
    'redpanda_cluster_controller_log_limit_requests_available_rps': 'controller.log_limit_requests_available',
    'redpanda_cluster_controller_log_limit_requests_dropped': 'controller.log_limit_requests_dropped',
}

VECTORIZED_CLUSTER = {
    'redpanda_kafka_max_offset': 'cluster.partition_committed_offset',
    'redpanda_kafka_partitions': 'cluster.partitions',
    'redpanda_kafka_replicas': 'cluster.replicas',
}

VECTORIZED_RPC = {
    'redpanda_rpc_active_connections': 'rpc.active_connections',
    'redpanda_rpc_request_errors_total': 'rpc.request_errors',
    'redpanda_rpc_request_latency_seconds': 'rpc.request_latency_seconds',
}

VECTORIZED_IO_QUEUE = {
    'redpanda_io_queue_total_read_ops': 'io_queue.total_read_ops',
    'redpanda_io_queue_total_write_ops': 'io_queue.total_write_ops',
}

VECTORIZED_KAFKA = {
    'redpanda_kafka_request_latency_seconds': 'kafka.request_latency_seconds',
    'redpanda_kafka_under_replicated_replicas': 'kafka.under_replicated_replicas',
    'redpanda_kafka_consumer_group_committed_offset': 'kafka.group_offset',
    'redpanda_kafka_consumer_group_consumers': 'kafka.group_count',
    'redpanda_kafka_consumer_group_topics': 'kafka.group_topic_count',
}

VECTORIZED_MEMORY = {
    'redpanda_memory_allocated_memory': 'memory.allocated_memory',
    'redpanda_memory_available_memory': 'memory.available_memory',
    'redpanda_memory_available_memory_low_water_mark': 'memory.available_memory_low_water_mark',
    'redpanda_memory_free_memory': 'memory.free_memory',
}

VECTORIZED_NODE_STATUS_RPC = {
    'redpanda_node_status_rpcs_received': 'node_status.rpcs_received',
    'redpanda_node_status_rpcs_sent': 'node_status.rpcs_sent',
    'redpanda_node_status_rpcs_timed_out': 'node_status.rpcs_timed_out',
}

VECTORIZED_PANDAPROXY = {
    'redpanda_rest_proxy_request_latency_seconds_sum': 'pandaproxy.request_latency',
    'redpanda_rest_proxy_request_errors_total': 'pandaproxy.request_errors',
}

VECTORIZED_CLUSTER_PARTITION = {
    'redpanda_cluster_partition_moving_from_node': 'partitions.moving_from_node',
    'redpanda_cluster_partition_moving_to_node': 'partitions.moving_to_node',
    'redpanda_cluster_partition_node_cancelling_movements': 'partitions.node_cancelling_movements',
}

VECTORIZED_RAFT = {
    'redpanda_raft_leadership_changes': 'raft.leadership_changes',
    'redpanda_raft_recovery_partition_movement_available_bandwidth': 'raft.recovery_bandwidth',
}

VECTORIZED_REACTOR = {
    'redpanda_cpu_busy_seconds_total': 'reactor.cpu_busy_ms',
}

VECTORIZED_SCHEDULER = {
    'redpanda_scheduler_runtime_seconds_total': 'scheduler.runtime_seconds',
}

VECTORIZED_SCHEMA_REGISTRY = {
    'redpanda_schema_registry_request_errors_total': 'schema_registry.errors',
    'redpanda_schema_registry_request_latency_seconds': 'schema_registry_latency_seconds',
}

VECTORIZED_STORAGE = {
    'redpanda_storage_disk_free_bytes': 'storage.disk_free_bytes',
    'redpanda_storage_disk_free_space_alert': 'storage.disk_free_space_alert',
    'redpanda_storage_disk_total_bytes': 'storage.disk_total_bytes',
}

INSTANCE_DEFAULT_METRICS = [
    VECTORIZED_APPLICATION,
    VECTORIZED_CLUSTER,
    VECTORIZED_CLUSTER_PARTITION,
    VECTORIZED_KAFKA,
    VECTORIZED_NODE_STATUS_RPC,
    VECTORIZED_PANDAPROXY,
    VECTORIZED_REACTOR,
    VECTORIZED_RPC,
    VECTORIZED_SCHEMA_REGISTRY,
    VECTORIZED_STORAGE,
]

ADDITIONAL_METRICS_MAP = {
    'redpanda.controller': VECTORIZED_CONTROLLER,
    'redpanda.io_queue': VECTORIZED_IO_QUEUE,
    'redpanda.memory': VECTORIZED_MEMORY,
    'redpanda.raft': VECTORIZED_RAFT,
    'redpanda.scheduler': VECTORIZED_SCHEDULER,
}
