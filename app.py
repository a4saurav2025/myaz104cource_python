from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Content structure based on AZ-104 outline
content = {
    'prerequisites': {
        'title': 'Prerequisites: AZ-104 Prerequisites for Azure Administrators',
        'description': 'Before diving into core topics, establish foundational knowledge of Azure administration tools, PowerShell, CLI, and ARM templates. This ensures you\'re comfortable with the environment.',
        'lessons': {
            1: {
                'title': 'Introduction to Azure Administration Tools',
                'description': 'Learn the essential tools for managing Azure resources, including portals, scripts, and templates.',
                'key_concepts': ['Azure Portal', 'PowerShell', 'Azure CLI', 'ARM templates', 'resource groups'],
                'tools': ['Azure Portal', 'PowerShell', 'Azure CLI'],
                'best_practices': ['Use ARM templates for repeatable deployments', 'always test scripts in a sandbox environment']
            },
            2: {
                'title': 'Managing Azure Resources with ARM Templates',
                'description': 'Understand how to deploy and manage resources declaratively using templates.',
                'key_concepts': ['Declarative vs. imperative deployment', 'template syntax', 'parameters', 'outputs'],
                'tools': ['Azure Resource Manager (ARM)', 'Visual Studio Code with ARM extensions'],
                'best_practices': ['Version control ARM templates', 'use parameters for flexibility and security']
            }
        }
    },
    'module1': {
        'title': 'Module 1: Manage Azure Identities and Governance (15-20% of Exam)',
        'description': 'Focus on securing and managing identities, access control, and organizational governance in Azure. This module builds trust and compliance foundations.',
        'lessons': {
            1: {
                'title': 'Understand Microsoft Entra ID',
                'description': 'Explore Microsoft Entra ID (formerly Azure AD) as a cloud identity service, comparing it to on-premises AD.',
                'key_concepts': ['Identity types (users, groups, service principals)', 'tenants', 'directories', 'Entra ID P1/P2 features', 'domain services'],
                'tools': ['Microsoft Entra admin center', 'Azure Portal'],
                'best_practices': ['Enable multi-factor authentication (MFA) for all users', 'regularly audit identities for unused accounts']
            },
            2: {
                'title': 'Create, Configure, and Manage Identities',
                'description': 'Learn to create and manage users, groups, and roles for secure access.',
                'key_concepts': ['User lifecycle', 'group management', 'role assignments', 'conditional access'],
                'tools': ['Microsoft Entra ID', 'Azure CLI', 'PowerShell'],
                'best_practices': ['Use least-privilege access', 'implement just-in-time (JIT) access for elevated permissions']
            },
            3: {
                'title': 'Describe Core Architectural Components of Azure',
                'description': 'Understand Azure\'s physical and management infrastructure for governance.',
                'key_concepts': ['Regions', 'availability zones', 'subscriptions', 'resource groups', 'management groups'],
                'tools': ['Azure Portal', 'Azure Resource Manager'],
                'best_practices': ['Organize resources into logical groups', 'use management groups for policy inheritance']
            },
            4: {
                'title': 'Azure Policy Initiatives',
                'description': 'Enforce organizational standards and assess compliance using policies.',
                'key_concepts': ['Policy definitions', 'initiatives', 'compliance evaluation', 'remediation'],
                'tools': ['Azure Policy', 'Azure Portal'],
                'best_practices': ['Start with built-in policies', 'use initiatives for grouped enforcement', 'monitor compliance regularly']
            },
            5: {
                'title': 'Secure Azure Resources with Azure RBAC',
                'description': 'Implement role-based access control to manage permissions.',
                'key_concepts': ['Roles (built-in/custom)', 'scopes', 'deny assignments', 'RBAC vs. ACLs'],
                'tools': ['Azure RBAC', 'Azure Portal', 'Azure CLI'],
                'best_practices': ['Assign roles at the lowest scope', 'use custom roles sparingly', 'audit role assignments']
            },
            6: {
                'title': 'Allow Users to Reset Passwords with Microsoft Entra Self-Service Password Reset',
                'description': 'Enable users to manage their own passwords securely.',
                'key_concepts': ['SSPR configuration', 'authentication methods', 'security questions'],
                'tools': ['Microsoft Entra admin center'],
                'best_practices': ['Require multiple verification methods', 'integrate with MFA for enhanced security']
            }
        }
    },
    'module2': {
        'title': 'Module 2: Implement and Manage Storage (15-20% of Exam)',
        'description': 'Dive into Azure Storage services for data management, security, and accessibility. This follows identity setup for secure storage access.',
        'lessons': {
            1: {
                'title': 'Configure Storage Accounts',
                'description': 'Set up storage accounts with appropriate replication and endpoints.',
                'key_concepts': ['Storage account types (GPv2, BlobStorage)', 'replication options (LRS, GRS)', 'endpoints', 'access tiers'],
                'tools': ['Azure Portal', 'Azure Storage Explorer', 'Azure CLI'],
                'best_practices': ['Choose replication based on data criticality', 'use secure transfer for HTTPS-only access']
            },
            2: {
                'title': 'Configure Azure Blob Storage',
                'description': 'Manage blob storage for unstructured data, including tiers and replication.',
                'key_concepts': ['Blob types (block, append, page)', 'access tiers (hot, cool, archive)', 'lifecycle policies'],
                'tools': ['Azure Blob Storage', 'AzCopy', 'Azure Storage Explorer'],
                'best_practices': ['Use lifecycle management to optimize costs', 'enable versioning for data protection']
            },
            3: {
                'title': 'Configure Azure Storage Security',
                'description': 'Secure storage with keys, signatures, and encryption.',
                'key_concepts': ['Shared access signatures (SAS)', 'encryption (at rest/transit)', 'firewalls', 'private endpoints'],
                'tools': ['Azure Key Vault', 'Azure Storage security features'],
                'best_practices': ['Rotate keys regularly', 'use SAS with minimal permissions and expiration times']
            },
            4: {
                'title': 'Configure Azure Files',
                'description': 'Set up file shares for cloud-based file storage and sync.',
                'key_concepts': ['File shares', 'Azure File Sync', 'SMB/NFS protocols', 'quotas'],
                'tools': ['Azure Files', 'Azure File Sync agent'],
                'best_practices': ['Use File Sync for hybrid scenarios', 'monitor usage to avoid overages']
            }
        }
    },
    'module3': {
        'title': 'Module 3: Deploy and Manage Azure Compute Resources (20-25% of Exam)',
        'description': 'Learn to deploy and scale compute resources like VMs, apps, and containers. This builds on storage for data-backed compute.',
        'lessons': {
            1: {
                'title': 'Introduction to Azure Virtual Machines',
                'description': 'Plan, create, and manage VMs for various workloads.',
                'key_concepts': ['VM sizes', 'images', 'disks', 'extensions', 'availability sets'],
                'tools': ['Azure Portal', 'Azure CLI', 'PowerShell'],
                'best_practices': ['Right-size VMs for cost efficiency', 'use managed disks for reliability']
            },
            2: {
                'title': 'Configure Virtual Machine Availability',
                'description': 'Ensure VM resilience with scaling and redundancy.',
                'key_concepts': ['Availability sets/zones', 'scale sets', 'load balancing'],
                'tools': ['Azure Virtual Machine Scale Sets', 'Azure Load Balancer'],
                'best_practices': ['Distribute VMs across zones', 'automate scaling based on metrics']
            },
            3: {
                'title': 'Configure Azure App Service Plans',
                'description': 'Set up hosting plans for web apps with scaling options.',
                'key_concepts': ['App Service plans (Free, Shared, Basic, etc.)', 'pricing tiers', 'scaling'],
                'tools': ['Azure App Service', 'Azure Portal'],
                'best_practices': ['Choose tiers based on traffic', 'enable auto-scaling for variable loads']
            },
            4: {
                'title': 'Configure Azure App Service',
                'description': 'Deploy and monitor web apps with deployment slots.',
                'key_concepts': ['App Service instances', 'deployment slots', 'custom domains', 'SSL'],
                'tools': ['Azure App Service', 'Git', 'Azure DevOps'],
                'best_practices': ['Use slots for staging', 'monitor performance with Application Insights']
            },
            5: {
                'title': 'Configure Azure Container Instances',
                'description': 'Run containers without managing VMs.',
                'key_concepts': ['Container groups', 'images', 'networking', 'volumes'],
                'tools': ['Azure Container Instances (ACI)', 'Docker'],
                'best_practices': ['Use for stateless workloads', 'integrate with Azure Container Registry']
            }
        }
    },
    'module4': {
        'title': 'Module 4: Implement and Manage Virtual Networking (20-25% of Exam)',
        'description': 'Configure secure and efficient networks for Azure resources. This integrates with compute and storage for connectivity.',
        'lessons': {
            1: {
                'title': 'Configure Virtual Networks',
                'description': 'Design and set up VNets with subnets and IP addressing.',
                'key_concepts': ['VNets', 'subnets', 'IP ranges', 'public/private IPs'],
                'tools': ['Azure Portal', 'Azure CLI'],
                'best_practices': ['Plan IP spaces to avoid conflicts', 'use private IPs for internal resources']
            },
            2: {
                'title': 'Configure Network Security Groups',
                'description': 'Control traffic with security rules.',
                'key_concepts': ['NSGs', 'inbound/outbound rules', 'priorities', 'application security groups'],
                'tools': ['Azure NSGs', 'Azure Portal'],
                'best_practices': ['Follow least-privilege', 'log and monitor rule hits']
            },
            3: {
                'title': 'Host Your Domain on Azure DNS',
                'description': 'Manage DNS zones and records for domain resolution.',
                'key_concepts': ['DNS zones', 'record types (A, CNAME)', 'custom domains'],
                'tools': ['Azure DNS', 'Azure Portal'],
                'best_practices': ['Use Azure DNS for public domains', 'enable DNSSEC for security']
            },
            4: {
                'title': 'Configure Azure Virtual Network Peering',
                'description': 'Connect VNets for seamless traffic flow.',
                'key_concepts': ['VNet peering', 'transit connectivity', 'global peering'],
                'tools': ['Azure VNet Peering'],
                'best_practices': ['Use for low-latency connections', 'avoid overlapping IP ranges']
            },
            5: {
                'title': 'Manage Traffic Flow with Routes',
                'description': 'Control routing in VNets with custom routes.',
                'key_concepts': ['Route tables', 'user-defined routes', 'BGP'],
                'tools': ['Azure Route Tables'],
                'best_practices': ['Implement forced tunneling for security', 'test routes before deployment']
            },
            6: {
                'title': 'Introduction to Azure Load Balancer',
                'description': 'Distribute traffic across resources.',
                'key_concepts': ['Load balancing types (public/internal)', 'health probes', 'rules'],
                'tools': ['Azure Load Balancer'],
                'best_practices': ['Use health probes', 'configure session persistence for stateful apps']
            },
            7: {
                'title': 'Introduction to Azure Application Gateway',
                'description': 'Manage web traffic with advanced routing.',
                'key_concepts': ['WAF', 'URL routing', 'SSL termination'],
                'tools': ['Azure Application Gateway'],
                'best_practices': ['Enable WAF for protection', 'use for microservices routing']
            },
            8: {
                'title': 'Introduction to Azure Network Watcher',
                'description': 'Monitor and troubleshoot network issues.',
                'key_concepts': ['Packet capture', 'NSG flow logs', 'connection troubleshoot'],
                'tools': ['Azure Network Watcher'],
                'best_practices': ['Enable diagnostics', 'use for proactive monitoring']
            }
        }
    },
    'module5': {
        'title': 'Module 5: Monitor and Maintain Azure Resources (10-15% of Exam)',
        'description': 'Conclude with monitoring health and backing up resources for reliability. This ensures ongoing management of all prior setups.',
        'lessons': {
            1: {
                'title': 'Introduction to Azure Backup',
                'description': 'Understand Azure\'s backup solutions for data protection.',
                'key_concepts': ['Backup vaults', 'recovery points', 'retention policies'],
                'tools': ['Azure Backup', 'Azure Portal'],
                'best_practices': ['Test restores regularly', 'use geo-redundant vaults for disaster recovery']
            },
            2: {
                'title': 'Protect Virtual Machines with Azure Backup',
                'description': 'Back up VMs and related workloads.',
                'key_concepts': ['VM backup', 'restore options', 'integration with Azure Site Recovery'],
                'tools': ['Azure Backup for VMs'],
                'best_practices': ['Schedule backups during off-peak', 'encrypt backups for security']
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
    # Find next and prev
    mod = content[module_id]
    lessons = list(mod['lessons'].keys())
    current_index = lessons.index(lesson_id)
    prev_lesson = lessons[current_index - 1] if current_index > 0 else None
    next_lesson = lessons[current_index + 1] if current_index < len(lessons) - 1 else None
    # If no next in module, go to next module's first lesson
    if not next_lesson:
        mod_index = modules.index(module_id)
        if mod_index < len(modules) - 1:
            next_mod = modules[mod_index + 1]
            next_lesson = 1
            next_module_id = next_mod
        else:
            next_module_id = None
    else:
        next_module_id = module_id
    # Prev similar
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
    return render_template('lesson.html', lesson=les, module_id=module_id, lesson_id=lesson_id, 
                           prev_module=prev_module_id, prev_lesson=prev_lesson, 
                           next_module=next_module_id, next_lesson=next_lesson)

if __name__ == '__main__':
    app.run(debug=True)