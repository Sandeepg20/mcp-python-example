from mcp.types import Tool, ToolInputSchema

def check_eligibility(input: ToolInputSchema) -> dict:
    """
    Simple business rule exposed as an MCP tool.
    """
    age = input.get("age")
    income = input.get("income")

    eligible = age >= 21 and income >= 30000

    return {
        "eligible": eligible,
        "reason": "Meets criteria" if eligible else "Does not meet criteria"
    }

check_eligibility_tool = Tool(
    name="check_eligibility",
    description="Check eligibility based on age and income",
    input_schema={
        "type": "object",
        "properties": {
            "age": {"type": "integer"},
            "income": {"type": "number"}
        },
        "required": ["age", "income"]
    },
    handler=check_eligibility
)

# Export tool reference
check_eligibility = check_eligibility_tool
