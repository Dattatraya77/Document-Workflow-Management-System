from django.core.exceptions import PermissionDenied


class WorkflowEngine:
    @staticmethod
    def perform_action(user, document_workflow, action):
        step = document_workflow.workflow.steps.get(step_order=document_workflow.current_step)


        if user.role != step.required_role:
            raise PermissionDenied("User not allowed for this step")


        if action == "approve":
            document_workflow.current_step += 1


            if document_workflow.current_step > document_workflow.workflow.steps.count():
                document_workflow.document.status = "APPROVED"
            else:
                document_workflow.document.status = "IN_REVIEW"


        elif action == "reject":
            document_workflow.document.status = "REJECTED"


        document_workflow.document.save()
        document_workflow.save()