---
name: threat-hunting
description: Proactive threat detection using Sigma rules, IOCs, and behavioral analytics
---

# Threat Hunting Skill

Proactive threat detection and investigation using detection rules, IOCs, and behavioral analytics.

## When to Use

- Threat hunting activities
- Suspicious behavior detection
- Security log analysis, IOC analysis
- Keywords: "threat", "hunt", "detection", "suspicious", "malware"

## Core Capabilities

### 1. Sigma Rule Analysis
- Rule interpretation/execution
- Custom rule creation
- False positive reduction

### 2. IOC Detection
- IP/domain reputation
- File hash lookups
- Process behavior monitoring

### 3. Behavioral Analytics
- Anomaly detection
- Baseline deviation
- Temporal pattern analysis

### 4. Log Analysis
- System log parsing
- Event correlation
- Timeline reconstruction

## Sigma Rule Example
```yaml
title: Suspicious PowerShell Download
logsource:
    product: windows
    service: powershell
detection:
    selection:
        EventID: 4104
        ScriptBlockText|contains:
            - 'DownloadString'
            - 'DownloadFile'
    condition: selection
level: medium
```

## Hunting Workflow

1. **Hypothesis**: Identify threats from intel, incidents, trends
2. **Data Collection**: Log sources, time range, normalization
3. **Analysis**: Apply rules, search IOCs, find anomalies
4. **Investigation**: Validate, eliminate false positives
5. **Response**: Escalate, remediate, update rules

## IOC Types

| Type | Examples |
|------|----------|
| Network | C2 IPs, malicious domains, unusual ports |
| File | Malware hashes, suspicious paths |
| Process | Bad process names, unusual parent-child |
| Registry | Persistence keys, malware artifacts |

## Quick Commands
```bash
# Log search
grep -i "suspicious_pattern" /var/log/auth.log

# Check connections
netstat -antp | grep ESTABLISHED

# Process analysis
ps aux | lsof -i -n -P
```

## MITRE ATT&CK Mapping

- Initial Access → Execution → Persistence
- Privilege Escalation → Defense Evasion
- Credential Access → Lateral Movement
- Collection → Exfiltration

## Best Practices

- ✅ Hypothesis-driven hunting
- ✅ Combine multiple data sources
- ✅ Document all findings
- ❌ Don't rely on single indicator
- ❌ Don't skip validation

## Integration

- **digital-forensics**: Evidence collection
- **log-analysis**: Advanced parsing
