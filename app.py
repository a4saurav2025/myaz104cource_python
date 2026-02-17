from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Content structure based on AZ-104 outline
# Module descriptions extended with 2-3 line "key concept" summaries.
content = {
    'prerequisites': {
        'title': 'Prerequisites: AZ-104 Prerequisites for Azure Administrators',
        'description': (
            "Before diving into core topics, establish foundational knowledge of Azure administration, "
            "PowerShell/CLI, and ARM templates. This ensures you\'re comfortable with the environment. "
            "Key concept: be able to automate and reproduce resource deployments reliably and safely."
        ),
        'lessons': {
            1: {
                'title': 'Introduction to Azure Administration Tools',
                'description': 'Learn the essential tools for managing Azure resources, including portals, scripts, and templates.',
                'key_concepts': ['Understanding how portal, CLI and scripting complement each other for management and automation.','When to use declarative templates vs. imperative commands.','Basic concepts of resource groups and idempotent deployments.'],
                'best_practices': [
                    'Use ARM templates for repeatable deployments',
                    'always test scripts in a sandbox environment',
                    'keep scripts and templates in version control',
                    'document required environment variables and service principals'
                ]
            },
            2: {
                'title': 'Managing Azure Resources with ARM Templates',
                'description': 'Understand how to deploy and manage resources declaratively using templates.',
                'key_concepts': ['Templates express desired state so deployments are repeatable and auditable.', 'Parameters and outputs make templates reusable across environments.', 'Validate templates before applying to production.'],
                'best_practices': [
                    'Version control ARM templates',
                    'use parameters for flexibility and security',
                    'validate templates with linting tools',
                    'create small reusable modules for common patterns'
                ]
            }
        }
    },
    'module1': {
        'title': 'Module 1: Manage Azure Identities and Governance (15-20% of Exam)',
        'description': (
            "Focus on securing and managing identities, access control, and organizational governance in Azure. "
            "Key concept: implement least-privilege identity and policy-driven governance so access and configuration scale securely."
        ),
        'lessons': {
            1: {
                'title': 'Understand Microsoft Entra ID',
                'description': 'Explore Microsoft Entra ID (formerly Azure AD) as a cloud identity service, comparing it to on-premises AD.',
                'key_concepts': ['Entra ID centralizes authentication and identity management for cloud services.', 'Tenant and directory boundaries matter for multi-tenant vs single-tenant apps.', 'Service principals enable secure app-to-Azure interactions.'],
                'best_practices': [
                    'Enable multi-factor authentication (MFA) for all users',
                    'regularly audit identities for unused accounts',
                    'use conditional access to reduce risk',
                    'monitor sign-in risk and configure identity protection policies'
                ]
            },
            2: {
                'title': 'Create, Configure, and Manage Identities',
                'description': 'Learn to create and manage users, groups, and roles for secure access.',
                'key_concepts': ['Manage identity lifecycle and enforce role-based access control (RBAC).', 'Group-based assignments scale permission management.', 'Use managed identities for service authentication rather than embedding credentials.'],
                'best_practices': [
                    'Use least-privilege access',
                    'implement just-in-time (JIT) access for elevated permissions',
                    'enforce strong onboarding/offboarding processes',
                    'document and review role assignments regularly'
                ]
            },
            3: {
                'title': 'Describe Core Architectural Components of Azure',
                'description': 'Understand Azure\'s physical and management infrastructure for governance.',
                'key_concepts': ['Regions and availability zones define fault domains and latency.', 'Subscriptions and management groups provide billing and policy scopes.', 'Resource groups organize resources logically for lifecycle management.'],
                'best_practices': [
                    'Organize resources into logical groups',
                    'use management groups for policy inheritance',
                    'apply tagging and naming standards for cost attribution',
                    'define subscription boundaries early to match organizational needs'
                ]
            },
            4: {
                'title': 'Azure Policy Initiatives',
                'description': 'Enforce organizational standards and assess compliance using policies.',
                'key_concepts': ['Policies evaluate resource state and can enforce or remediate non-compliance.', 'Initiatives group policies for easier assignment and auditing.', 'Use policy exemptions carefully and document them.'],
                'best_practices': [
                    'Start with built-in policies',
                    'use initiatives for grouped enforcement',
                    'monitor compliance regularly',
                    'test policy effects in non-production before wide rollout'
                ]
            },
            5: {
                'title': 'Secure Azure Resources with Azure RBAC',
                'description': 'Implement role-based access control to manage permissions.',
                'key_concepts': ['RBAC assigns permissions at scopes to enforce least privilege.', 'Built-in roles cover common needs; custom roles fill specific gaps.', 'Audit and review role assignments frequently.'],
                'best_practices': [
                    'Assign roles at the lowest scope',
                    'use custom roles sparingly',
                    'audit role assignments',
                    'prefer role assignment via groups rather than individual users'
                ]
            },
            6: {
                'title': 'Allow Users to Reset Passwords with Microsoft Entra Self-Service Password Reset',
                'description': 'Enable users to manage their own passwords securely.',
                'key_concepts': ['SSPR reduces help-desk load while preserving security controls.', 'Require multiple verification methods to reduce account takeover risk.'],
                'best_practices': [
                    'Require multiple verification methods',
                    'integrate with MFA for enhanced security',
                    'educate users on secure recovery methods',
                    'monitor SSPR usage and investigate anomalies'
                ]
            }
        }
    },
    'module2': {
        'title': 'Module 2: Implement and Manage Storage (15-20% of Exam)',
        'description': (
            "Dive into Azure Storage services for data management, security, and accessibility. "
            "Key concept: choose the right storage tier, redundancy and access model to balance cost, performance and resilience."
        ),
        'lessons': {
            1: {
                'title': 'Configure Storage Accounts',
                'description': 'Set up storage accounts with appropriate replication and endpoints.',
                'key_concepts': ['Storage accounts provide namespaces and determine replication/feature set.', 'Replication choice affects durability and cost trade-offs.'],
                'best_practices': [
                    'Choose replication based on data criticality',
                    'use secure transfer for HTTPS-only access',
                    'apply network rules and private endpoints where possible',
                    'use tagging for cost reporting and lifecycle policies'
                ]
            },
            2: {
                'title': 'Configure Azure Blob Storage',
                'description': 'Manage blob storage for unstructured data, including tiers and replication.',
                'key_concepts': ['Blob access tiers control cost vs. retrieval latency.', 'Lifecycle policies automate tiering and retention for cost management.'],
                'best_practices': [
                    'Use lifecycle management to optimize costs',
                    'enable versioning for data protection',
                    'enable soft delete for accidental deletes',
                    'monitor access patterns and adjust tiers accordingly'
                ]
            },
            3: {
                'title': 'Configure Azure Storage Security',
                'description': 'Secure storage with keys, signatures, and encryption.',
                'key_concepts': ['SAS tokens grant scoped, time-limited access; rotate and limit scope.', 'Always encrypt data at rest and use private endpoints to restrict network access.'],
                'best_practices': [
                    'Rotate keys regularly',
                    'use SAS with minimal permissions and expiration times',
                    'store secrets in Key Vault and use RBAC for access control',
                    'audit access logs for anomalous activity'
                ]
            },
            4: {
                'title': 'Configure Azure Files',
                'description': 'Set up file shares for cloud-based file storage and sync.',
                'key_concepts': ['Azure Files provides SMB/NFS-compatible file shares for lift-and-shift scenarios.', 'File Sync enables caching and tiering across on-prem and cloud.'],
                'best_practices': [
                    'Use File Sync for hybrid scenarios',
                    'monitor usage to avoid overages',
                    'secure file shares with NTFS permissions and identity-based access',
                    'plan quotas and tiering to reduce costs'
                ]
            }
        }
    },
    'module3': {
        'title': 'Module 3: Deploy and Manage Azure Compute Resources (20-25% of Exam)',
        'description': (
            "Learn to deploy and scale compute resources like VMs, apps, and containers. "
            "Key concept: design for resilience and operational efficiency using managed services and automation."
        ),
        'lessons': {
            1: {
                'title': 'Introduction to Azure Virtual Machines',
                'description': 'Plan, create, and manage VMs for various workloads.',
                'key_concepts': ['Choose appropriate VM sizes and storage options based on workload needs.', 'Use managed disks for durability and simplified management.'],
                'best_practices': [
                    'Right-size VMs for cost efficiency',
                    'use managed disks for reliability',
                    'automate image and configuration management',
                    'implement patching and backup schedules'
                ]
            },
            2: {
                'title': 'Configure Virtual Machine Availability',
                'description': 'Ensure VM resilience with scaling and redundancy.',
                'key_concepts': ['Availability sets/zones and scale sets improve fault tolerance and scaling.', 'Design for graceful degradation and automate scaling based on metrics.'],
                'best_practices': [
                    'Distribute VMs across zones',
                    'automate scaling based on metrics',
                    'use health probes and automated remediation',
                    'test failover scenarios regularly'
                ]
            },
            3: {
                'title': 'Configure Azure App Service Plans',
                'description': 'Set up hosting plans for web apps with scaling options.',
                'key_concepts': ['App Service plans determine the compute resources and scaling behavior of Web Apps.', 'Choose a pricing tier that matches availability, scaling, and feature needs.'],
                'best_practices': [
                    'Choose tiers based on traffic',
                    'enable auto-scaling for variable loads',
                    'use deployment slots to minimize downtime',
                    'monitor app performance and tweak plan size accordingly'
                ]
            },
            4: {
                'title': 'Configure Azure App Service',
                'description': 'Deploy and monitor web apps with deployment slots.',
                'key_concepts': ['Use deployment slots for zero-downtime deployments and safe rollbacks.', 'Integrate with CI/CD for repeatable releases.'],
                'best_practices': [
                    'Use slots for staging',
                    'monitor performance with Application Insights',
                    'secure app settings with managed identities',
                    'apply TLS and strong cipher policies for custom domains'
                ]
            },
            5: {
                'title': 'Configure Azure Container Instances',
                'description': 'Run containers without managing VMs.',
                'key_concepts': ['ACI is suitable for short-lived or burst container workloads without orchestration.', 'Use images from trusted registries and keep images minimal for faster startup.'],
                'best_practices': [
                    'Use for stateless workloads',
                    'integrate with Azure Container Registry',
                    'scan container images for vulnerabilities',
                    'set appropriate resource limits to avoid noisy neighbors'
                ]
            }
        }
    },
    'module4': {
        'title': 'Module 4: Implement and Manage Virtual Networking (20-25% of Exam)',
        'description': (
            "Configure secure and efficient networks for Azure resources. "
            "Key concept: design segmented, monitored networks that enforce security boundaries and enable scalable connectivity."
        ),
        'lessons': {
            1: {
                'title': 'Configure Virtual Networks',
                'description': 'Design and set up VNets with subnets and IP addressing.',
                'key_concepts': ['Plan IP addressing to avoid overlap and enable hybrid connectivity.', 'Subnets and network security boundaries simplify traffic control.'],
                'best_practices': [
                    'Plan IP spaces to avoid conflicts',
                    'use private IPs for internal resources',
                    'document network design and usage patterns',
                    'reserve address space for future growth'
                ]
            },
            2: {
                'title': 'Configure Network Security Groups',
                'description': 'Control traffic with security rules.',
                'key_concepts': ['NSGs control traffic flow at the subnet or NIC level using allow/deny rules.', 'Use application security groups to group VMs with similar rules.'],
                'best_practices': [
                    'Follow least-privilege',
                    'log and monitor rule hits',
                    'use tags and naming conventions for rules',
                    'periodically review and tighten rules'
                ]
            },
            3: {
                'title': 'Host Your Domain on Azure DNS',
                'description': 'Manage DNS zones and records for domain resolution.',
                'key_concepts': ['DNS is foundational to name resolution and service discovery.', 'Protect DNS zones and enable DNSSEC for critical domains.'],
                'best_practices': [
                    'Use Azure DNS for public domains',
                    'enable DNSSEC for security',
                    'automate record updates where possible',
                    'monitor TTL impacts on failover scenarios'
                ]
            },
            4: {
                'title': 'Configure Azure Virtual Network Peering',
                'description': 'Connect VNets for seamless traffic flow.',
                'key_concepts': ['Peering provides low-latency connectivity between VNets without gateways.', 'Design peering and transitive patterns carefully to avoid routing complexity.'],
                'best_practices': [
                    'Use for low-latency connections',
                    'avoid overlapping IP ranges',
                    'document peering topology',
                    'use network virtual appliances only when necessary'
                ]
            },
            5: {
                'title': 'Manage Traffic Flow with Routes',
                'description': 'Control routing in VNets with custom routes.',
                'key_concepts': ['User-defined routes enable traffic steering to appliances or on-premises networks.', 'Validate route precedence and next-hop choices carefully.'],
                'best_practices': [
                    'Implement forced tunneling for security',
                    'test routes before deployment',
                    'maintain a route documentation and diagram',
                    'monitor for unexpected route changes'
                ]
            },
            6: {
                'title': 'Introduction to Azure Load Balancer',
                'description': 'Distribute traffic across resources.',
                'key_concepts': ['Load balancers distribute traffic using health probes and rules for scale and availability.', 'Choose the correct layer (L4 vs L7) based on application needs.'],
                'best_practices': [
                    'Use health probes',
                    'configure session persistence for stateful apps',
                    'test failover and scaling behavior',
                    'monitor backend health continuously'
                ]
            },
            7: {
                'title': 'Introduction to Azure Application Gateway',
                'description': 'Manage web traffic with advanced routing.',
                'key_concepts': ['Application Gateway provides L7 routing and WAF capabilities for web applications.', 'Use URL-based routing and WAF rules to protect web workloads.'],
                'best_practices': [
                    'Enable WAF for protection',
                    'use for microservices routing',
                    'tune WAF rules to reduce false positives',
                    'use TLS termination where appropriate'
                ]
            },
            8: {
                'title': 'Introduction to Azure Network Watcher',
                'description': 'Monitor and troubleshoot network issues.',
                'key_concepts': ['Network Watcher provides diagnostics like packet captures and connection troubleshooting.', 'Use flow logs for security investigations and traffic analysis.'],
                'best_practices': [
                    'Enable diagnostics',
                    'use for proactive monitoring',
                    'archive logs for forensic investigations',
                    'integrate with SIEM for alerting'
                ]
            }
        }
    },
    'module5': {
        'title': 'Module 5: Monitor and Maintain Azure Resources (10-15% of Exam)',
        'description': (
            "Conclude with monitoring health and backing up resources for reliability. "
            "Key concept: implement observability and recovery plans so services remain reliable and recoverable."
        ),
        'lessons': {
            1: {
                'title': 'Introduction to Azure Backup',
                'description': 'Understand Azure\'s backup solutions for data protection.',
                'key_concepts': ['Backup vaults centralize backup policies and retention.', 'Recovery objectives drive backup frequency and retention settings.'],
                'best_practices': [
                    'Test restores regularly',
                    'use geo-redundant vaults for disaster recovery',
                    'define RPO/RTO and validate them with drills',
                    'encrypt backups and manage keys securely'
                ]
            },
            2: {
                'title': 'Protect Virtual Machines with Azure Backup',
                'description': 'Back up VMs and related workloads.',
                'key_concepts': ['VM backup protects OS and data disks and integrates with recovery services.', 'Consider application-consistent snapshots for critical workloads.'],
                'best_practices': [
                    'Schedule backups during off-peak',
                    'encrypt backups for security',
                    'validate backup integrity periodically',
                    'automate backup policy application across resource groups'
                ]
            }
        }
    }
}

# List of modules in order
modules = ['prerequisites', 'module1', 'module2', 'module3', 'module4', 'module5']

@app.route('/')
def home():
    return render_template('index.html', modules=modules, content=content)

@app.route('/module/<module_id>')
def module(module_id):
    if module_id not in content:
        return 'Module not found', 404
    mod = content[module_id]
    return render_template('module.html', module=mod, module_id=module_id, lessons=mod['lessons'])

@app.route('/lesson/<module_id>/<int:lesson_id>')
def lesson(module_id, lesson_id):
    if module_id not in content or lesson_id not in content[module_id]['lessons']:
        return 'Lesson not found', 404
    les = content[module_id]['lessons'][lesson_id]

    # Navigation: only within the same module (do NOT auto-advance to next module)
    mod = content[module_id]
    lessons = list(mod['lessons'].keys())
    current_index = lessons.index(lesson_id)

    # Previous: allow moving to the previous lesson; if none in this module, keep existing behavior
    prev_lesson = lessons[current_index - 1] if current_index > 0 else None
    if not prev_lesson:
        mod_index = modules.index(module_id)
        if mod_index > 0:
            prev_mod = modules[mod_index - 1]
            prev_lessons = list(content[prev_mod]['lessons'].keys())
            prev_lesson = prev_lessons[-1]
            prev_module_id = prev_mod
        else:
            prev_module_id = None
    else:
        prev_module_id = module_id

    # Next: only move to the next lesson inside the SAME module. Do NOT provide a "next" that jumps to another module.
    next_lesson = lessons[current_index + 1] if current_index < len(lessons) - 1 else None
    next_module_id = module_id if next_lesson else None

    return render_template('lesson.html', lesson=les, module_id=module_id, lesson_id=lesson_id,
                           prev_module=prev_module_id, prev_lesson=prev_lesson,
                           next_module=next_module_id, next_lesson=next_lesson)


@app.route('/resources')
def resources():
    """Return a single-page view containing short descriptions for all modules and lessons.
    This aggregates every resource (module → lesson) into one page for quick reference.
    """
    all_resources = []
    for mod_id in modules:
        mod = content[mod_id]
        for lesson_id, lesson in mod['lessons'].items():
            all_resources.append({
                'module_id': mod_id,
                'module_title': mod['title'],
                'module_description': mod.get('description', ''),
                'lesson_id': lesson_id,
                'title': lesson.get('title'),
                'description': lesson.get('description'),
                'key_concepts': lesson.get('key_concepts', []),
                'best_practices': lesson.get('best_practices', [])
            })
    return render_template('resources.html', all_resources=all_resources)

if __name__ == '__main__':
    app.run(debug=True)