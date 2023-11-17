# Incident Postmortem: Nginx Server Port Misconfiguration

## Issue Summary

**Duration:**
- Start Time: November 2nd, 2023, 22:43 WAT
- End Time: November 2nd, 2023, 23:01 WAT

**Impact:**
- The Nginx server experienced an outage, rendering web pages inaccessible.
- Users were unable to access the affected service during the outage.
- Approximately 33% of users were impacted.

**Root Cause:**
- The root cause of the issue was a recent misconfiguration that caused the Nginx server to listen on the wrong port, deviating from the standard port 80 configuration. Additionally, the server was not restarted after the configuration change.

## Timeline

**Detection:**
- The issue was detected on November 2nd, 2023, 22:43 WAT by Datadog monitoring alerts.

**Actions Taken:**
- Investigation focused on recent configuration changes.
- Assumptions included potential network issues or upstream service problems.

**Escalation:**
- The incident was escalated to the SRE/Development team responsible for server infrastructure.

**Resolution:**
- The Nginx server was reconfigured to listen on the correct port (port 80).
- A server restart was performed to apply the configuration changes.
- Normal service was restored, and users regained access to the web pages.

## Root Cause and Resolution

**Root Cause Explanation:**
- The issue stemmed from a recent configuration change that altered the Nginx server's port settings. The server was mistakenly configured to listen on a non-standard port, causing disruptions in service delivery.

**Resolution Details:**
- The corrective action involved reverting the Nginx configuration to the standard port 80 settings.
- A server restart was executed to apply the corrected configuration.
- Thorough testing confirmed the restoration of proper functionality.

## Corrective and Preventative Measures

**Improvements/Fixes:**
- Enhance change management processes to include thorough testing before applying configurations in production.
- Implement automated monitoring for Nginx server configurations, triggering alerts for deviations from standard settings.

**Tasks to Address the Issue:**
- Conduct a review of recent configuration changes to identify potential discrepancies.
- Updated notes to emphasize the importance of restarting services after configuration modifications.
- Plan regular times to audit server configurations to identify and rectify issues.

This incident postmortem outlines the key aspects of the Nginx server outage, including the duration, impact, root cause, timeline of events, resolution details, and proposed corrective/preventative measures. The focus is on clarity and brevity, providing essential information for both technical and non-technical stakeholders.

