from moto.core.exceptions import RESTError


class ELBClientError(RESTError):
    code = 400


class DuplicateTagKeysError(ELBClientError):
    def __init__(self, cidr):
        super().__init__(
            "DuplicateTagKeys", "Tag key was specified more than once: {0}".format(cidr)
        )


class LoadBalancerNotFoundError(ELBClientError):
    def __init__(self):
        super().__init__(
            "LoadBalancerNotFound", "The specified load balancer does not exist."
        )


class ListenerNotFoundError(ELBClientError):
    def __init__(self):
        super().__init__("ListenerNotFound", "The specified listener does not exist.")


class SubnetNotFoundError(ELBClientError):
    def __init__(self):
        super().__init__("SubnetNotFound", "The specified subnet does not exist.")


class TargetGroupNotFoundError(ELBClientError):
    def __init__(self):
        super().__init__(
            "TargetGroupNotFound", "The specified target group does not exist."
        )


class TooManyTagsError(ELBClientError):
    def __init__(self):
        super().__init__(
            "TooManyTagsError",
            "The quota for the number of tags that can be assigned to a load balancer has been reached",
        )


class BadHealthCheckDefinition(ELBClientError):
    def __init__(self):
        super().__init__(
            "ValidationError",
            "HealthCheck Target must begin with one of HTTP, TCP, HTTPS, SSL",
        )


class DuplicateListenerError(ELBClientError):
    def __init__(self):
        super().__init__(
            "DuplicateListener", "A listener with the specified port already exists."
        )


class DuplicateLoadBalancerName(ELBClientError):
    def __init__(self):
        super().__init__(
            "DuplicateLoadBalancerName",
            "A load balancer with the specified name already exists.",
        )


class DuplicateTargetGroupName(ELBClientError):
    def __init__(self):
        super().__init__(
            "DuplicateTargetGroupName",
            "A target group with the specified name already exists.",
        )


class InvalidTargetError(ELBClientError):
    def __init__(self):
        super().__init__(
            "InvalidTarget",
            "The specified target does not exist or is not in the same VPC as the target group.",
        )


class EmptyListenersError(ELBClientError):
    def __init__(self):
        super().__init__("ValidationError", "Listeners cannot be empty")


class PriorityInUseError(ELBClientError):
    def __init__(self):
        super().__init__("PriorityInUse", "The specified priority is in use.")


class InvalidConditionFieldError(ELBClientError):
    VALID_FIELDS = [
        "path-pattern",
        "host-header",
        "http-header",
        "http-request-method",
        "query-string",
        "source-ip",
    ]

    def __init__(self, invalid_name):
        super().__init__(
            "ValidationError",
            "Condition field '%s' must be one of '[%s]'"
            % (invalid_name, ",".join(self.VALID_FIELDS)),
        )


class InvalidConditionValueError(ELBClientError):
    def __init__(self, msg):
        super().__init__("ValidationError", msg)


class InvalidActionTypeError(ELBClientError):
    def __init__(self, invalid_name, index):
        super().__init__(
            "ValidationError",
            "1 validation error detected: Value '%s' at 'actions.%s.member.type' failed to satisfy constraint: Member must satisfy enum value set: [forward, redirect, fixed-response]"
            % (invalid_name, index),
        )


class ActionTargetGroupNotFoundError(ELBClientError):
    def __init__(self, arn):
        super().__init__("TargetGroupNotFound", "Target group '%s' not found" % arn)


class ListenerOrBalancerMissingError(ELBClientError):
    def __init__(self):
        super().__init__(
            "ValidationError",
            "You must specify either listener ARNs or a load balancer ARN",
        )


class InvalidDescribeRulesRequest(ELBClientError):
    def __init__(self, msg):
        super().__init__("ValidationError", msg)


class ResourceInUseError(ELBClientError):
    def __init__(self, msg="A specified resource is in use"):
        super().__init__("ResourceInUse", msg)


class RuleNotFoundError(ELBClientError):
    def __init__(self):
        super().__init__("RuleNotFound", "The specified rule does not exist.")


class DuplicatePriorityError(ELBClientError):
    def __init__(self, invalid_value):
        super().__init__(
            "ValidationError",
            "Priority '%s' was provided multiple times" % invalid_value,
        )


class InvalidTargetGroupNameError(ELBClientError):
    def __init__(self, msg):
        super().__init__("ValidationError", msg)


class InvalidModifyRuleArgumentsError(ELBClientError):
    def __init__(self):
        super().__init__(
            "ValidationError", "Either conditions or actions must be specified"
        )


class InvalidStatusCodeActionTypeError(ELBClientError):
    def __init__(self, msg):
        super().__init__("ValidationError", msg)


class InvalidLoadBalancerActionException(ELBClientError):
    def __init__(self, msg):
        super().__init__("InvalidLoadBalancerAction", msg)
