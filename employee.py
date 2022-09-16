import uuid

JOB_TITLES = ["SALES_REP", "REGIONAL_MANAGER", "MANAGER", "HR", "ACCOUNTING"]


class Employee:
    def __init__(self, name: str, job_title: str):
        self.name = name
        self.job_title = job_title
        self.employee_id = uuid.uuid4()

    def update_contact_info(self, name: str) -> str:
        """
        Method which updates the contact info of this employee
        :param name: New name for this employee
        :return: str: the previous name of this employee
        """
        past_name = self.name
        self.name = name
        return past_name

    def promote_employee(self, job_title):
        """
        Promote this employee to a new job title
        :param job_title: The new job title for this employee
        :return: None
        """
        if job_title not in JOB_TITLES:
            raise ValueError(
                f"Invalid job title {job_title}, expected one of {JOB_TITLES}"
            )
        self.job_title = job_title
