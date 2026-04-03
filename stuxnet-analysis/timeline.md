# Stuxnet Timeline

## Discovery and Attribution

| Date | Event |
|------|-------|
| **Jan 2010** | First known infections detected in Iran, though the malware was likely deployed as early as 2007-2009 |
| **Jun 2010** | VirusBlokAda (Belarus) identifies a new malware sample spreading via USB drives and exploiting a Windows Shell LNK vulnerability (CVE-2010-2568) |
| **Jul 2010** | Siemens acknowledges the malware targets its SIMATIC WinCC/Step 7 SCADA software |
| **Jul 2010** | Microsoft issues emergency patch for the LNK vulnerability (MS10-046) |
| **Sep 2010** | Symantec publishes initial detailed analysis revealing the malware targets specific Siemens S7-300 PLCs controlling variable-frequency drives |
| **Nov 2010** | Iran acknowledges Stuxnet damaged centrifuges at Natanz, with President Ahmadinejad confirming problems with "electronic components" |
| **Nov 2010** | Symantec reveals Stuxnet targets two specific frequency converter models — made by Fararo Paya (Iran) and Vacon (Finland) — operating at frequencies consistent with uranium enrichment centrifuge operation (807-1210 Hz) |
| **Feb 2011** | Symantec releases the comprehensive W32.Stuxnet Dossier (Version 1.4) |
| **Jun 2012** | David Sanger (New York Times) reports on "Olympic Games," attributing Stuxnet to a joint U.S.-Israeli operation based on sources within the Obama administration |
| **2013** | Ralph Langner publishes "To Kill a Centrifuge," the most detailed technical analysis of Stuxnet's PLC payload |
| **2014** | Kim Zetter publishes "Countdown to Zero Day," the definitive journalistic account |

## Technical Evolution

Researchers identified at least two major versions:

- **Stuxnet 0.5** (2007-2009): Earlier, more cautious variant that manipulated centrifuge valve operations. Used a different C&C mechanism and fewer propagation methods.
- **Stuxnet 1.x** (2009-2010): The version that was publicly discovered. More aggressive propagation, targeted centrifuge motor speeds, and included four zero-day exploits.

## Impact Assessment

- An estimated 1,000 of Iran's 9,000 centrifuges at Natanz were destroyed or degraded
- Iran's nuclear program was delayed by an estimated 1-2 years
- The malware spread to over 100,000 systems in 115+ countries, though it only activated its destructive payload on systems matching the specific Natanz configuration
