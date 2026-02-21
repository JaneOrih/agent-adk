from jinja2 import Template

import json

data = {
    "user_id": "user123",
    "session_id": "session456",
    "query": "What is the AI platform's governance posture?",
    "organization": {
        "company_name": "TechCorp",
        "legal_entity_name": "TechCorp Ltd.",
        "industry": "Artificial Intelligence",
        "primary_hq_country": "USA",
        "website": "https://www.techcorp.com/"
    },
    "operating_context": {
        "operating_countries": ["USA", "Canada", "Germany"],
        "ai_operating_domain": "Healthcare",
        "regulatory_exposure": "GDPR, HIPAA"
    },
    "governance_posture": {
        "audit_strictness": "High",
        "risk_appetite": "Moderate",
        "autonomy_level": "Medium",
        "change_control_level": "High",
        "new_agent_requires_approval": True,
        "requested_exceptions": ["None"]
    },
    "execution_authority": {
        "human_override_allowed": True,
        "policy_enforced_pre_execution": True,
        "policy_enforced_post_execution": True
    },
    "platform_boundary": {
        "ownership": "TechCorp",
        "tool_access_scope": "Internal",
        "model_access_scope": "External and Internal"
    },
    "data_governance": {
        "data_classes": ["Personal Data", "Health Data", "Financial Data"],
        "retention_preference": "5 years",
        "data_residency_required": True
    },
    "identity_and_access": {
        "identity_provider_type": "OAuth2",
        "private_network_required": True
    },
    "cloud_and_infra": {
        "cloud_posture": "Private Cloud",
        "deployment_model": "Hybrid"
    },
    "ai_platform_intent": {
        "ai_platform_scope": "Global",
        "initial_use_case_types": ["Medical Diagnostics", "Predictive Analytics"],
        "model_policy": "Ethical and Transparent",
        "existing_ai_platform_maturity": "Advanced",
        "reuse_preference": "Reuse existing models",
        "declared_constraints": "None"
    }
}


with open("sample2.md", "r") as f:
    markdown_template= f.read()

template = Template(markdown_template)

populated_markdown = template.render(
    user_id=data["user_id"],
    session_id=data["session_id"],
    query=data["query"],
    current_date="2026-02-19",  
    company_name=data["organization"]["company_name"],
    legal_entity_name=data["organization"]["legal_entity_name"],
    industry=data["organization"]["industry"],
    primary_hq_country=data["organization"]["primary_hq_country"],
    website=data["organization"]["website"],
    operating_countries=", ".join(data["operating_context"]["operating_countries"]),
    ai_operating_domain=data["operating_context"]["ai_operating_domain"],
    regulatory_exposure=data["operating_context"]["regulatory_exposure"],
    audit_strictness=data["governance_posture"]["audit_strictness"],
    risk_appetite=data["governance_posture"]["risk_appetite"],
    autonomy_level=data["governance_posture"]["autonomy_level"],
    change_control_level=data["governance_posture"]["change_control_level"],
    new_agent_requires_approval=data["governance_posture"]["new_agent_requires_approval"],
    requested_exceptions=", ".join(data["governance_posture"]["requested_exceptions"]),
    human_override_allowed=data["execution_authority"]["human_override_allowed"],
    policy_enforced_pre_execution=data["execution_authority"]["policy_enforced_pre_execution"],
    policy_enforced_post_execution=data["execution_authority"]["policy_enforced_post_execution"],
    ownership=data["platform_boundary"]["ownership"],
    tool_access_scope=data["platform_boundary"]["tool_access_scope"],
    model_access_scope=data["platform_boundary"]["model_access_scope"],
    data_classes=", ".join(data["data_governance"]["data_classes"]),
    retention_preference=data["data_governance"]["retention_preference"],
    data_residency_required=data["data_governance"]["data_residency_required"],
    identity_provider_type=data["identity_and_access"]["identity_provider_type"],
    private_network_required=data["identity_and_access"]["private_network_required"],
    cloud_posture=data["cloud_and_infra"]["cloud_posture"],
    deployment_model=data["cloud_and_infra"]["deployment_model"],
    ai_platform_scope=data["ai_platform_intent"]["ai_platform_scope"],
    initial_use_case_types=", ".join(data["ai_platform_intent"]["initial_use_case_types"]),
    model_policy=data["ai_platform_intent"]["model_policy"],
    existing_ai_platform_maturity=data["ai_platform_intent"]["existing_ai_platform_maturity"],
    reuse_preference=data["ai_platform_intent"]["reuse_preference"],
    declared_constraints=data["ai_platform_intent"]["declared_constraints"]
)

# Output the populated markdown to a file
with open("ai_governance_framework.md", "w") as f:
    f.write(populated_markdown)

print("Markdown file has been populated and saved.")



import markdown
from weasyprint import HTML

# Step 1: Load the populated markdown content
with open('ai_governance_framework.md', 'r') as file:
    markdown_content = file.read()

# Step 2: Convert markdown to HTML
html_content = markdown.markdown(markdown_content)

# Step 3: Convert HTML to PDF using WeasyPrint
HTML(string=html_content).write_pdf("ai_governance_framework.pdf")

print("PDF has been successfully generated.")