# Changelog

All notable changes to the Cascading Hybrid Thermal Scavenger (CHTS) project will be documented in this file.

The format is inspired by Keep a Changelog and follows semantic project evolution where possible.

---

## [v1.0.0] - 2026-05-25
### Finalized Modeled Architecture Release

This release marks the first internally consistent, thermodynamically credible, and reproducible modeled CHTS platform.

### Added
- Sequential thermodynamic cascade controller
- Dynamic Carnot-limited recovery modeling
- Deterministic modeled uncertainty (`modeled_sigma`)
- Validation ledger generation pipeline
- Telemetry QA validation tools
- Dynamic timestamped ledger generation
- Zeotropic recovery manager integration
- PCM thermal buffering support
- Analytics and performance visualization tooling
- Controller → telemetry → ledger → validation workflow

### Changed
- Transitioned from coefficient-stacked recovery to serial enthalpy depletion
- Reworked thermal recovery logic to model remaining heat between stages
- Updated visualization to use independent thermodynamic boundary logic
- Improved telemetry realism with drift and transient behavior
- Refined validation language to classify outputs as calibrated model prediction
- Standardized package exports and controller API
- Synced analytics, tests, and validation artifacts

### Fixed
- Package import inconsistencies
- Analytics/controller desynchronization
- Ledger generation runtime path issues
- Validation schema mismatch issues
- Visualization double-Carnot calculation bug
- RNG reproducibility inconsistencies
- Legacy architecture remnants and stale references
- Broken telemetry validation alignment

### Removed
- Magnetohydrodynamic (MHD) subsystem and associated architecture
- Legacy MHD validation artifacts
- Deprecated controller methods
- Obsolete efficiency assumptions and stale analytics references

### Validation Status
Current release represents:

- Thermodynamically credible modeled system
- Reproducible engineering software
- Internal validation and traceability complete

Experimental hardware validation remains future work.

---

## [Pre-v1 Development]
### Historical Development Summary

Earlier development generations included:

- Experimental MHD-assisted concepts
- Parallel recovery models
- Legacy node architectures
- Early coefficient-driven recovery simulations
- Multiple controller and analytics redesigns

These versions were progressively retired in favor of the current serial cascade thermal recovery framework.
