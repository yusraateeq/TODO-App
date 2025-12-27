# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)

All development MUST follow the mandatory workflow: Constitution → Specs → Plan → Tasks → Implement.

**Non-negotiable Rules:**
- No agent may write code without approved specs and tasks
- Specs define what; plans define how; tasks define implementation order
- Code changes require corresponding spec/plan/task updates
- Refinement MUST occur at spec level, not code level
- User stories MUST be independently testable for incremental delivery

### II. Agent Behavior Rules

Agents MUST adhere to the following constraints:

**Human Interaction:**
- Humans do NOT write code manually; agents execute all implementation
- Agents MUST NOT invent features not in approved specifications
- Agents MUST NOT deviate from approved specifications
- Clarification requests MUST be surfaced when requirements are ambiguous

**Specification Discipline:**
- Feature requests require specification before implementation
- Specification changes require plan updates
- Plan changes require task reassessment
- All changes flow upward through the hierarchy

### III. Phase Governance

The project is divided into distinct phases (I through V), each with strict boundaries:

**Phase Scoping:**
- Each phase is strictly scoped by its specification document
- Future-phase features MUST NOT leak into earlier phases
- Phase completion requires all user stories in that phase to be complete
- Phase boundaries are enforced at the specification level

**Architecture Evolution:**
- Architecture may only evolve through updated specs and plans
- Cross-phase architectural decisions require phase-n specification
- Breaking changes require ADR documentation and migration plans
- Phase transitions require explicit user sign-off

### IV. Technology Stack Constraints

The following technology stack is mandated:

**Backend (All Phases):**
- Python for backend services
- FastAPI for API framework
- SQLModel for ORM and data modeling
- Neon DB for PostgreSQL database

**Frontend (Phases III-V):**
- Next.js for frontend framework

**AI & Agents (Phases II-V):**
- OpenAI Agents SDK for agent orchestration
- MCP (Model Context Protocol) for tool integration

**Infrastructure (Phases IV-V):**
- Docker for containerization
- Kubernetes for orchestration
- Kafka for event streaming
- Dapr for distributed application runtime

### V. Quality Principles

All code MUST adhere to these quality standards:

**Architecture:**
- Clean architecture with clear separation of concerns
- Stateless services where required for scalability
- Dependency injection for testability
- SOLID principles applied consistently

**Cloud-Native Readiness:**
- 12-factor app principles for configuration and deployment
- Container-first design (Phases IV-V)
- Horizontal scaling designed into architecture
- Observability built-in (logs, metrics, traces)

**Code Quality:**
- Single responsibility per module
- Explicit over implicit (no magic, clear intent)
- Testable code (dependency-injected, mockable)
- Documentation for all public interfaces

## Technology Constraints

**Mandatory Stack:**
- Python 3.11+
- FastAPI 0.100+
- SQLModel
- Neon DB (PostgreSQL)

**Conditional Stack (by Phase):**
- Next.js 14+ (Phases III-V)
- OpenAI Agents SDK (Phases II-V)
- MCP (Phases II-V)
- Docker 24+ (Phases IV-V)
- Kubernetes 1.28+ (Phases IV-V)
- Kafka 3.0+ (Phases IV-V)
- Dapr 1.12+ (Phases IV-V)

**Prohibited:**
- No monolithic architectures spanning multiple bounded contexts
- No synchronous cross-service calls without circuit breakers (Phases IV-V)
- No hardcoded secrets; all secrets via environment variables
- No blocking I/O in hot paths

## Development Workflow

**Specification Phase:**
1. User describes feature intent
2. Agent creates spec.md with user stories and requirements
3. Agent creates plan.md with technical approach
4. Agent creates tasks.md with implementation steps
5. User approves all documents
6. Implementation begins

**Implementation Phase:**
1. Tasks executed in dependency order
2. Tests written before implementation (Test-First)
3. Red-Green-Refactor cycle enforced
4. Each user story tested independently
5. Commit after each task or logical group

**Quality Gates:**
- All tests MUST pass before merge
- Linting and formatting MUST pass
- Type checking MUST pass
- Documentation MUST be updated

## Governance

**Constitution Supremacy:**
This constitution is the supreme governing document for all agents.
All other practices, templates, and procedures are subordinate to it.

**Amendment Process:**
1. Amendment proposed via user request
2. Impact analysis performed and documented
3. Version incremented (MAJOR for breaking changes, MINOR for additions, PATCH for clarifications)
4. Templates updated to reflect new principles
5. All agents notified of changes

**Versioning Policy:**
- MAJOR: Backward-incompatible governance or principle changes
- MINOR: New principles added or materially expanded guidance
- PATCH: Clarifications, wording fixes, non-semantic refinements

**Compliance Review:**
- All plans MUST reference constitution principles
- All implementations MUST comply with quality principles
- Deviations MUST be documented in Complexity Tracking table
- Violations MUST be flagged and justified

**References:**
- Runtime guidance: See `CLAUDE.md` for agent-specific instructions
- Templates: See `.specify/templates/` for spec/plan/task templates
- History: See `history/prompts/` for PHR records, `history/adr/` for architectural decisions

**Version**: 1.0.0 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27
