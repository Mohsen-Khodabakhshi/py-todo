from enum import Enum


class TaskPriority(str, Enum):
    PRIORITY_LOW = "low"
    PRIORITY_NORMAL = "normal"
    PRIORITY_HIGH = "high"
    PRIORITY_CRITICAL = "critical"


class ProjectUserStatus(str, Enum):
    INVITED = 'invited'
    ACCEPTED_INVITE = 'accepted_invite'
    REJECTED_INVITE = 'rejected_invite'
