from _typeshed import Incomplete

from influxdb_client.domain.notification_rule_discriminator import NotificationRuleDiscriminator

class SMTPNotificationRuleBase(NotificationRuleDiscriminator):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: Incomplete | None = None,
        subject_template: Incomplete | None = None,
        body_template: Incomplete | None = None,
        to: Incomplete | None = None,
        latest_completed: Incomplete | None = None,
        last_run_status: Incomplete | None = None,
        last_run_error: Incomplete | None = None,
        id: Incomplete | None = None,
        endpoint_id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        task_id: Incomplete | None = None,
        owner_id: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        status: Incomplete | None = None,
        name: Incomplete | None = None,
        sleep_until: Incomplete | None = None,
        every: Incomplete | None = None,
        offset: Incomplete | None = None,
        runbook_link: Incomplete | None = None,
        limit_every: Incomplete | None = None,
        limit: Incomplete | None = None,
        tag_rules: Incomplete | None = None,
        description: Incomplete | None = None,
        status_rules: Incomplete | None = None,
        labels: Incomplete | None = None,
        links: Incomplete | None = None,
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def subject_template(self): ...
    @subject_template.setter
    def subject_template(self, subject_template) -> None: ...
    @property
    def body_template(self): ...
    @body_template.setter
    def body_template(self, body_template) -> None: ...
    @property
    def to(self): ...
    @to.setter
    def to(self, to) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
