# Fail-Safe Protocols: GEN-III CHTS

## 1. Objective
To maintain system integrity and prevent thermal runaway in the event of controller power loss, sensor failure, or structural damage.

## 2. Emergency Shutdown Sequences
- **Loss of Power (Controller Failure):** All active shunts default to the "Open" position. The zeotropic loop transitions to a passive thermosiphon mode, utilizing natural convection to dump heat to the primary radiator.
- **Over-Temperature Event (> 150°C):** A mechanical thermal fuse ruptures, diverting the primary heat input stream away from the TEG array and directly into the secondary PCM buffer (Emergency Sink).
- **PCM Containment Breach:** Automated vacuum-lock valves in the adsorption beds close to isolate chemical components and prevent atmospheric contamination.

## 3. Passive Safety Features
- **Redundancy:** The zeotropic loop is designed for natural circulation; no external pumping is required to move fluid during an emergency state.
- **Mechanical Shunts:** All bypass valves are spring-loaded to the "Open" position, ensuring that the system cannot be trapped in a "High-Input/Zero-Recovery" state.

## 4. Post-Incident Recovery
- Following a fail-safe trigger, the system must undergo a manual reset and an integrity scan of the semiconductor junctions (TEG) and adsorption bed vacuum seals before power-up.
