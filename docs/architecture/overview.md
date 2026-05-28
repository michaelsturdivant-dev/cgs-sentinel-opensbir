# Architecture Overview

CGS Sentinel OpenSBIR™ is organized as a public reference implementation.

## Layers

1. **API Layer** — FastAPI endpoints for projects, opportunities, work items, artifacts, and dashboard summaries.
2. **Schema Layer** — Public Pydantic models for non-sensitive request and response structures.
3. **Routing Layer** — Simple keyword-based public reference routing.
4. **Documentation Layer** — SBIR, OTA, grant, and commercialization documentation.

## Excluded Protected Layer

The proprietary CGS Sentinel AI Engine™, including advanced kernels, agent chains, private prompts, commercial dashboards, client data, and implementation playbooks, is excluded from this repository.
