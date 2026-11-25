# CrewAI Integrations Examples

This directory contains examples demonstrating how to integrate CrewAI with other frameworks, platforms, and model providers.

## Examples in this Directory

### 1. CrewAI-LangGraph
Integration between CrewAI and LangGraph for advanced workflow orchestration:
- Combines CrewAI's agent capabilities with LangGraph's graph-based execution
- Demonstrates state management across frameworks
- Shows how to leverage both tools' strengths

### 2. Azure Model
Using CrewAI with Azure OpenAI services:
- Configuration for Azure-hosted models
- Authentication setup
- Enterprise deployment patterns

### 3. NVIDIA Models
Integration with NVIDIA's AI model ecosystem:
- Using NVIDIA-hosted models
- Performance optimization examples
- Multiple example implementations (intro, marketing strategy)


### 4. AiEnsured agentest
Offline behavioral testing for recorded CrewAI traces using `agentest-ai`:
- Runs 165 deterministic checks without an LLM judge or API key
- Catches success claims after failed tool calls, ungrounded outputs, and out-of-order actions
- Exports CrewAI tool events to OpenTelemetry GenAI traces for CI regression checks

## Integration Patterns

These examples demonstrate:
- **Model Provider Flexibility**: Using different LLM providers
- **Framework Interoperability**: Combining CrewAI with other AI frameworks
- **Enterprise Deployments**: Cloud-specific configurations
- **Custom Model Endpoints**: Working with specialized model services

## Getting Started

Each integration example includes specific setup instructions for:
- API key configuration
- Authentication requirements
- Dependencies and environment setup
- Platform-specific considerations

Choose an integration based on your infrastructure needs and follow the example-specific documentation.