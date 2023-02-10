import os

from datadog_checks.dev import get_docker_hostname

HOST = get_docker_hostname()
PORT = 9644

INSTANCE_PORT = 9644
INSTANCE_URL = "http://{}:{}/public_metrics".format(HOST, INSTANCE_PORT)


REDPANDA_VERSION = os.getenv('REDPANDA_VERSION')

MOCK_REDPANDA_INSTANCE = {'openmetrics_endpoint': INSTANCE_URL, 'tags': ['instance_test']}

CHECK_NAME = 'redpanda'

INSTANCE_METRIC_GROUP_MAP = {
    'redpanda.application': [
        'redpanda.application.uptime',
        'redpanda.application.build',
    ],
    'redpanda.controller': [
        'redpanda.controller.log_limit_requests_available',
        'redpanda.controller.log_limit_requests_dropped.count',
    ],
    'redpanda.cluster': [
        'redpanda.cluster.partition_committed_offset',
        'redpanda.cluster.partitions',
        'redpanda.cluster.replicas',
    ],
    'redpanda.rpc': [
        'redpanda.rpc.active_connections',
        # 'redpanda.rpc.request_errors',
        'redpanda.rpc.request_latency_seconds.count',
        'redpanda.rpc.request_latency_seconds.bucket',
        'redpanda.rpc.request_latency_seconds.sum',
    ],
    'redpanda.io_queue': [
        'redpanda.io_queue.total_read_ops.count',
        'redpanda.io_queue.total_write_ops.count',
    ],
    'redpanda.kafka': [
        'redpanda.kafka.request_latency_seconds.sum',
        'redpanda.kafka.request_latency_seconds.bucket',
        'redpanda.kafka.request_latency_seconds.count',
        'redpanda.kafka.under_replicated_replicas',
        'redpanda.kafka.group_offset',
        'redpanda.kafka.group_count',
        'redpanda.kafka.group_topic_count',
    ],
    'redpanda.memory': [
        'redpanda.memory.allocated_memory',
        'redpanda.memory.available_memory',
        'redpanda.memory.available_memory_low_water_mark',
        'redpanda.memory.free_memory',
    ],
    'redpanda.node_status': [
        'redpanda.node_status.rpcs_received',
        'redpanda.node_status.rpcs_sent',
        'redpanda.node_status.rpcs_timed_out',
    ],
    # 'redpanda.pandaproxy': [
    #    'redpanda.pandaproxy.request_latency',
    #    'redpanda.pandaproxy.request_errors',
    # ],
    'redpanda.partitions': [
        'redpanda.partitions.moving_from_node',
        'redpanda.partitions.moving_to_node',
        'redpanda.partitions.node_cancelling_movements',
    ],
    'redpanda.raft': [
        'redpanda.raft.leadership_changes.count',
        'redpanda.raft.recovery_bandwidth',
    ],
    'redpanda.reactor': [
        'redpanda.reactor.cpu_busy_ms',
    ],
    'redpanda.scheduler': [
        # 'redpanda.scheduler.runtime_seconds',
    ],
    'redpanda.schema_registry': [
        # 'redpanda.schema_registry.errors',
        'redpanda.schema_registry_latency_seconds.count',
        'redpanda.schema_registry_latency_seconds.bucket',
        'redpanda.schema_registry_latency_seconds.sum',
    ],
    'redpanda.storage': [
        'redpanda.storage.disk_free_bytes.count',
        'redpanda.storage.disk_free_space_alert',
        'redpanda.storage.disk_total_bytes.count',
    ],
}
# fmt: on

INSTANCE_DEFAULT_GROUPS = [
    'redpanda.application',
    'redpanda.cluster',
    'redpanda.rpc',
    'redpanda.kafka',
    'redpanda.node_status',
    #    'redpanda.pandaproxy',
    'redpanda.partitions',
    'redpanda.reactor',
    'redpanda.schema_registry',
    'redpanda.storage',
]

INSTANCE_ADDITIONAL_GROUPS = [
    'redpanda.controller',
    'redpanda.io_queue',
    'redpanda.memory',
    'redpanda.raft',
    'redpanda.scheduler',
]


def get_metrics(metric_groups):
    """Given a list of metric groups, return single consolidated list"""
    return sorted(m for g in metric_groups for m in INSTANCE_METRIC_GROUP_MAP[g])


INSTANCE_DEFAULT_METRICS = get_metrics(INSTANCE_DEFAULT_GROUPS)
INSTANCE_ADDITIONAL_METRICS = get_metrics(INSTANCE_ADDITIONAL_GROUPS)
