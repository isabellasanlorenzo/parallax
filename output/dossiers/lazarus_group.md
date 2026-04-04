# Threat Actor Dossier: Lazarus Group
> MITRE ATT&CK Group ID: **G0032**
> Generated: 2026-04-04 04:20 UTC  |  Sources: mitre_attack, alienvault_otx, malpedia

## Synopsis

Lazarus Group is a North Korean state-sponsored cyber threat actor attributed to the Reconnaissance General Bureau (RGB) that has maintained an active operational presence since at least 2009. The group pursues espionage and financial crime objectives across government, private sector, and energy targets through a comprehensive tradecraft approach spanning resource development, defense evasion, command and control, discovery, and execution techniques. Lazarus Group operates a sophisticated malware arsenal including RawDisk, BADCALL, FALLCHILL, WannaCry, MagicRAT, HOPLIGHT, and TYPEFRAME, demonstrating technical capability to conduct both destructive and persistent campaigns. The group is responsible for high-profile operations including the November 2014 Sony Pictures Entertainment wiper attack and the documented Operation Dream Job campaign. Lazarus Group's operational profile encompasses 93 distinct ATT&CK techniques, reflecting a mature and diversified cyber threat capability with sustained targeting across multiple sectors and geographies.

## Overview

| Field | Value |
|---|---|
| **Origin** | North Korea |
| **First Seen** | 2009 |
| **Motivations** | espionage, financial crime |
| **Also Known As** | Labyrinth Chollima, HIDDEN COBRA, Guardians of Peace, ZINC, NICKEL ACADEMY, Diamond Sleet, Operation DarkSeoul, Dark Seoul, Hastati Group, Andariel, Unit 121, Bureau 121, NewRomanic Cyber Army Team, Bluenoroff, Subgroup: Bluenoroff, Group 77, Operation Troy, Operation GhostSecret, Operation AppleJeus, APT38, APT 38, Stardust Chollima, Whois Hacking Team, Appleworm, APT-C-26, NICKEL GLADSTONE, COVELLITE, ATK3, G0032, ATK117, G0082, Citrine Sleet, DEV-0139, DEV-1222, Sapphire Sleet, COPERNICIUM, TA404, Lazarus group, BeagleBoyz, Moonstone Sleet, Black Artemis, Lazarus, Genie Spider |

## TTP Table

| Technique ID | Tactic | Name | Confidence |
|---|---|---|---|
| T1001.003 | Command and Control | Protocol or Service Impersonation | MEDIUM |
| T1005 | Collection | Data from Local System | MEDIUM |
| T1008 | Command and Control | Fallback Channels | MEDIUM |
| T1010 | Discovery | Application Window Discovery | MEDIUM |
| T1012 | Discovery | Query Registry | MEDIUM |
| T1016 | Discovery | System Network Configuration Discovery | MEDIUM |
| T1021.001 | Lateral Movement | Remote Desktop Protocol | MEDIUM |
| T1021.002 | Lateral Movement | SMB/Windows Admin Shares | MEDIUM |
| T1021.004 | Lateral Movement | SSH | MEDIUM |
| T1027.007 | Defense Evasion | Dynamic API Resolution | MEDIUM |
| T1027.009 | Defense Evasion | Embedded Payloads | MEDIUM |
| T1027.013 | Defense Evasion | Encrypted/Encoded File | MEDIUM |
| T1033 | Discovery | System Owner/User Discovery | MEDIUM |
| T1036.003 | Defense Evasion | Rename Legitimate Utilities | MEDIUM |
| T1036.004 | Defense Evasion | Masquerade Task or Service | MEDIUM |
| T1036.005 | Defense Evasion | Match Legitimate Resource Name or Location | MEDIUM |
| T1041 | Exfiltration | Exfiltration Over C2 Channel | MEDIUM |
| T1046 | Discovery | Network Service Discovery | MEDIUM |
| T1047 | Execution | Windows Management Instrumentation | MEDIUM |
| T1048.003 | Exfiltration | Exfiltration Over Unencrypted Non-C2 Protocol | MEDIUM |
| T1049 | Discovery | System Network Connections Discovery | MEDIUM |
| T1053.005 | Execution | Scheduled Task | MEDIUM |
| T1055.001 | Defense Evasion | Dynamic-link Library Injection | MEDIUM |
| T1056.001 | Collection | Keylogging | MEDIUM |
| T1057 | Discovery | Process Discovery | MEDIUM |
| T1059.001 | Execution | PowerShell | MEDIUM |
| T1059.003 | Execution | Windows Command Shell | MEDIUM |
| T1059.005 | Execution | Visual Basic | MEDIUM |
| T1070 | Defense Evasion | Indicator Removal | MEDIUM |
| T1070.003 | Defense Evasion | Clear Command History | MEDIUM |
| T1070.004 | Defense Evasion | File Deletion | MEDIUM |
| T1070.006 | Defense Evasion | Timestomp | MEDIUM |
| T1071.001 | Command and Control | Web Protocols | MEDIUM |
| T1074.001 | Collection | Local Data Staging | MEDIUM |
| T1078 | Defense Evasion | Valid Accounts | MEDIUM |
| T1082 | Discovery | System Information Discovery | MEDIUM |
| T1083 | Discovery | File and Directory Discovery | MEDIUM |
| T1090.001 | Command and Control | Internal Proxy | MEDIUM |
| T1090.002 | Command and Control | External Proxy | MEDIUM |
| T1098 | Persistence | Account Manipulation | MEDIUM |
| T1102.002 | Command and Control | Bidirectional Communication | MEDIUM |
| T1104 | Command and Control | Multi-Stage Channels | MEDIUM |
| T1105 | Command and Control | Ingress Tool Transfer | MEDIUM |
| T1106 | Execution | Native API | MEDIUM |
| T1110.003 | Credential Access | Password Spraying | MEDIUM |
| T1124 | Discovery | System Time Discovery | MEDIUM |
| T1132.001 | Command and Control | Standard Encoding | MEDIUM |
| T1134.002 | Defense Evasion | Create Process with Token | MEDIUM |
| T1140 | Defense Evasion | Deobfuscate/Decode Files or Information | MEDIUM |
| T1189 | Initial Access | Drive-by Compromise | MEDIUM |
| T1202 | Defense Evasion | Indirect Command Execution | MEDIUM |
| T1203 | Execution | Exploitation for Client Execution | MEDIUM |
| T1204.002 | Execution | Malicious File | MEDIUM |
| T1218 | Defense Evasion | System Binary Proxy Execution | MEDIUM |
| T1218.005 | Defense Evasion | Mshta | MEDIUM |
| T1218.011 | Defense Evasion | Rundll32 | MEDIUM |
| T1485 | Impact | Data Destruction | MEDIUM |
| T1489 | Impact | Service Stop | MEDIUM |
| T1491.001 | Impact | Internal Defacement | MEDIUM |
| T1529 | Impact | System Shutdown/Reboot | MEDIUM |
| T1542.003 | Persistence | Bootkit | MEDIUM |
| T1543.003 | Persistence | Windows Service | MEDIUM |
| T1547.001 | Persistence | Registry Run Keys / Startup Folder | MEDIUM |
| T1547.009 | Persistence | Shortcut Modification | MEDIUM |
| T1553.002 | Defense Evasion | Code Signing | MEDIUM |
| T1557.001 | Credential Access | LLMNR/NBT-NS Poisoning and SMB Relay | MEDIUM |
| T1560 | Collection | Archive Collected Data | MEDIUM |
| T1560.002 | Collection | Archive via Library | MEDIUM |
| T1560.003 | Collection | Archive via Custom Method | MEDIUM |
| T1561.001 | Impact | Disk Content Wipe | MEDIUM |
| T1561.002 | Impact | Disk Structure Wipe | MEDIUM |
| T1562.001 | Defense Evasion | Disable or Modify Tools | MEDIUM |
| T1562.004 | Defense Evasion | Disable or Modify System Firewall | MEDIUM |
| T1564.001 | Defense Evasion | Hidden Files and Directories | MEDIUM |
| T1566.001 | Initial Access | Spearphishing Attachment | MEDIUM |
| T1566.002 | Initial Access | Spearphishing Link | MEDIUM |
| T1566.003 | Initial Access | Spearphishing via Service | MEDIUM |
| T1571 | Command and Control | Non-Standard Port | MEDIUM |
| T1573.001 | Command and Control | Symmetric Cryptography | MEDIUM |
| T1574.001 | Persistence | DLL | MEDIUM |
| T1574.013 | Persistence | KernelCallbackTable | MEDIUM |
| T1583.001 | Resource Development | Domains | MEDIUM |
| T1583.006 | Resource Development | Web Services | MEDIUM |
| T1584.004 | Resource Development | Server | MEDIUM |
| T1585.001 | Resource Development | Social Media Accounts | MEDIUM |
| T1585.002 | Resource Development | Email Accounts | MEDIUM |
| T1587.001 | Resource Development | Malware | MEDIUM |
| T1588.002 | Resource Development | Tool | MEDIUM |
| T1588.004 | Resource Development | Digital Certificates | MEDIUM |
| T1589.002 | Reconnaissance | Email Addresses | MEDIUM |
| T1591 | Reconnaissance | Gather Victim Org Information | MEDIUM |
| T1620 | Defense Evasion | Reflective Code Loading | MEDIUM |
| T1680 | Discovery | Local Storage Discovery | MEDIUM |

## Indicators of Compromise (OTX: 36)

| Type | Value | Confidence | Threat Type | Malware Family | First Seen |
|---|---|---|---|---|---|
| cve | CVE-2017-7269 |  |  |  |  |
| domain | daedong[.]or[.]kr |  |  |  |  |
| domain | kcnp[.]or[.]kr |  |  |  |  |
| domain | kosic[.]or[.]kr |  |  |  |  |
| domain | wstore[.]lt |  |  |  |  |
| domain | xkclub[.]hk |  |  |  |  |
| hash_md5 | b270e83bf3344427b37d1cc5893b6a2c |  |  |  |  |
| hash_md5 | 41c145fb05b9c870028babb2a2826dc8 |  |  |  |  |
| hash_md5 | 97d290e7c38f26bd6ae9127ef2305314 |  |  |  |  |
| hash_md5 | 022aeb126d2d80e683f7f2a3ee920874 |  |  |  |  |
| hash_md5 | 8c2c9d5d3d8a6830882b228ac316bc18 |  |  |  |  |
| hash_md5 | 38f39e8b0aae9fbc77f430013ab95179 |  |  |  |  |
| hash_md5 | 53f0c7426b8ef437bb62044869608d4f |  |  |  |  |
| hash_md5 | 7876c0ce16e5e566df9ef9c34807c4f6 |  |  |  |  |
| hash_md5 | 4eaaa684e1257bf16418a5cfc500d19b |  |  |  |  |
| hash_md5 | 50b9197ae56c02465d69e9eb53c54fca |  |  |  |  |
| hash_sha1 | 57648a0ac01c44d958f7084ba5b9758770932b26 |  |  |  |  |
| hash_sha1 | 17e22b7755e7cca0c04d1b6bff9ed338980697ce |  |  |  |  |
| hash_sha1 | 088ebb266859a252c3a961abf6c3319fbd281e76 |  |  |  |  |
| hash_sha1 | bae7cf01d1c55ded40cb015214fe517b41819b29 |  |  |  |  |
| hash_sha1 | 2f0949e081f807aa0b6b3d8fc34e2435c427cfba |  |  |  |  |
| hash_sha1 | be6b8264df0602b67ad7c74e670f9a14986f7f23 |  |  |  |  |
| hash_sha1 | 6a22c48d7dcde9eebc5789a16863d13235801bb5 |  |  |  |  |
| hash_sha1 | 20903749acd37da9dc5db8117d8e46300363fadb |  |  |  |  |
| hash_sha1 | 3f6166e37b3916f23ab47a11bb0c9d0ce5d62fa0 |  |  |  |  |
| hash_sha1 | 6fc4ce2046e8eddbdc41eee756037d2172f92c27 |  |  |  |  |
| hash_sha256 | 15d6881ad5e7e7fe8c1db4b00149b4e0ef5a920b591dd21a64b487658c8e54c8 |  |  |  |  |
| hash_sha256 | df7912d7618e9859b918b4b9dd1d754f10ee4ea34942ed20b8850c5a94c59fb6 |  |  |  |  |
| hash_sha256 | 4618ce48c8da41415bec0fd0668f8f4a2244011f9891bd8ea70e6224f8e7d58b |  |  |  |  |
| hash_sha256 | ebba2aa065059f1f841a86100905310d11e1b8d7a0f8e89bc1227b19ab69e9af |  |  |  |  |
| hash_sha256 | b7e4d0359e8723733c8cf871b809af77d43445be84140f94ce55e5b1149e36de |  |  |  |  |
| hash_sha256 | 8aaaff59ef34398603294a092b66c1029f9f10508dd3cbecda9d16764c36ddf4 |  |  |  |  |
| hash_sha256 | a681dc3c390a64f7d72f2359cd7e77b40ff804d0640e67fd542203ad6cb0e96c |  |  |  |  |
| hash_sha256 | 030156f455617ef8e092beedf95c7ce2840594af30d2bb9ac49608a75e123aa6 |  |  |  |  |
| hash_sha256 | 184a1dd3580b5441d5139c0a45b838483f1a5eb4a16f00fd6b1585e692adb96c |  |  |  |  |
| hash_sha256 | 1458f86d4415b9ca81114d017b8169da3457a9293cb3b388dfae6b48abd76c9d |  |  |  |  |

## Targeted Sectors

- Government
- Private sector
- Energy

## Associated Malware / Tools

| Name | Type | Description |
|---|---|---|
| RawDisk | malware | RawDisk is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks,… |
| Proxysvc | malware | Proxysvc is a malicious DLL used by Lazarus Group in a campaign known as Operation GhostSecret. It has appeared to be… |
| BADCALL | malware | BADCALL is a Trojan malware variant used by the group Lazarus Group. (Citation: US-CERT BADCALL) |
| FALLCHILL | malware | FALLCHILL is a RAT that has been used by Lazarus Group since at least 2016 to target the aerospace, telecommunications,… |
| WannaCry | malware | WannaCry is ransomware that was first seen in a global attack during May 2017, which affected more than 150 countries.… |
| MagicRAT | malware | MagicRAT is a remote access tool developed in C++ and exclusively used by the Lazarus Group threat actor in operations.… |
| HOPLIGHT | malware | HOPLIGHT is a backdoor Trojan that has reportedly been used by the North Korean government.(Citation: US-CERT HOPLIGHT… |
| TYPEFRAME | malware | TYPEFRAME is a remote access tool that has been used by Lazarus Group. (Citation: US-CERT TYPEFRAME June 2018) |
| Dtrack | malware | Dtrack is spyware that was discovered in 2019 and has been used against Indian financial institutions, research… |
| HotCroissant | malware | HotCroissant is a remote access trojan (RAT) attributed by U.S. government entities to malicious North Korean… |
| HARDRAIN | malware | HARDRAIN is a Trojan malware variant reportedly used by the North Korean government. (Citation: US-CERT HARDRAIN March… |
| Dacls | malware | Dacls is a multi-platform remote access tool used by Lazarus Group since at least December 2019.(Citation: TrendMicro… |
| KEYMARBLE | malware | KEYMARBLE is a Trojan that has reportedly been used by the North Korean government. (Citation: US-CERT KEYMARBLE Aug… |
| TAINTEDSCRIBE | malware | TAINTEDSCRIBE is a fully-featured beaconing implant integrated with command modules used by Lazarus Group. It was first… |
| AuditCred | malware | AuditCred is a malicious DLL that has been used by Lazarus Group during their 2018 attacks.(Citation: TrendMicro… |
| netsh | malware | netsh is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet… |
| ECCENTRICBANDWAGON | malware | ECCENTRICBANDWAGON is a remote access Trojan (RAT) used by North Korean cyber actors that was first identified in… |
| AppleJeus | malware | AppleJeus is a family of downloaders initially discovered in 2018 embedded within trojanized cryptocurrency… |
| route | malware | route can be used to find or change information within the local system IP routing table. (Citation: TechNet Route) |
| BLINDINGCAN | malware | BLINDINGCAN is a remote access Trojan that has been used by the North Korean government since at least early 2020 in… |
| ThreatNeedle | malware | ThreatNeedle is a backdoor that has been used by Lazarus Group since at least 2019 to target cryptocurrency, defense,… |
| Volgmer | malware | Volgmer is a backdoor Trojan designed to provide covert access to a compromised system. It has been used since at least… |
| Cryptoistic | malware | Cryptoistic is a backdoor, written in Swift, that has been used by Lazarus Group.(Citation: SentinelOne Lazarus macOS… |
| Responder | malware | Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue… |
| RATANKBA | malware | RATANKBA is a remote controller tool used by Lazarus Group. RATANKBA has been used in attacks targeting financial… |
| Bankshot | malware | Bankshot is a remote access tool (RAT) that was first reported by the Department of Homeland Security in December of… |
| Unidentified 101 (Lazarus?) | malware | Potential Lazarus sample. |
| Unidentified 090 (Lazarus) | malware | Recon/Loader malware attributed to Lazarus, disguised as Notepad++ shell extension. |
| SpectralBlur | malware |  |
| QUICKCAFE | malware | QUICKCAFE is an encrypted JavaScript downloader for QUICKRIDE.POWER that exploits the ActiveX M2Soft vulnerabilities.… |
| 3CX Backdoor | malware |  |
| Casso | malware |  |
| Interception | malware |  |
| Unidentified macOS 001 (UnionCryptoTrader) | malware |  |
| WatchCat | malware |  |
| Yort | malware |  |
| RedHat Hacker WebShell | malware |  |
| PowerBrace | malware |  |
| PowerSpritz | malware |  |
| BLINDTOAD | malware | BLINDTOAD is 64-bit Service DLL that loads an encrypted file from disk and executes it in memory. |
| BUFFETLINE | malware |  |
| CLEANTOAD | malware | CLEANTOAD is a disruption tool that will delete file system artifacts, including those related to BLINDTOAD, and will… |
| Klackring | malware | Microsoft describes that threat actor ZINC is using Klackring as a malware dropped by ComeBacker, both being used to… |
| PowerRatankba | malware | QUICKRIDE.POWER is a PowerShell variant of the QUICKRIDE backdoor. Its payloads are often saved to C:\windows\temp\ |
| RustBucket | malware |  |
| sRDI | malware | sRDI allows for the conversion of DLL files to position independent shellcode. It attempts to be a fully functional PE… |
| DarkComet | malware | DarkComet is one of the most famous RATs, developed by Jean-Pierre Lesueur in 2008. After being used in the Syrian… |
| FastCash | malware |  |
| HLOADER | malware |  |

## Campaigns

### Operation Dream Job (2019-09-01T04:00:00.000Z – 2020-08-01T04:00:00.000Z)

Operation Dream Job was a cyber espionage operation likely conducted by Lazarus Group that targeted the defense, aerospace, government, and other sectors in the United States, Israel, Australia, Russia, and India. In at least one case, the cyber actors tried to monetize their network access to conduct a business email compromise (BEC) operation. In 2020, security researchers noted overlapping TTPs, to include fake job lures and code similarities, between Operation Dream Job, Operation North Star, and Operation Interception; by 2022 security researchers described Operation Dream Job as an umbrella term covering both Operation Interception and Operation North Star.(Citation: ClearSky Lazarus Aug 2020)(Citation: McAfee Lazarus Jul 2020)(Citation: ESET Lazarus Jun 2020)(Citation: The Hacker News Lazarus Aug 2022)

