from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Parse the az.txt file and create structured data
def parse_az_txt():
    with open('az.txt', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Section mappings
    sections = {
        'Azure Basics': [
            'Azure Portal', 'Azure CLI', 'Azure Powershell',
            'Azure Resource Manager', 'Azure Pricing', 'Azure Security Centre',
            'Azure Advisor'
        ],
        'Manage Azure Identities and Governance': [
            'Azure Active Directory', 'Azure Role-Based Access Control',
            'Azure Policy', 'Azure Service Health'
        ],
        'Implement and Manage Storage': [
            'Azure Key Vault', 'Azure Blob service', 'Azure File Storage',
            'Azure Disk Storage', 'Azure Queue Storage', 'Azure Table Storage',
            'Azure Archive Storage'
        ],
        'Deploy and Manage Azure Compute Resources': [
            'Azure Virtual Machine', 'Azure App Service', 'Application Service Environments',
            'Azure Container Registry', 'Azure Container Instances', 'Azure Kubernetes Service'
        ],
        'Configure and Manage Virtual Networking': [
            'Azure Virtual Network', 'Azure DNS', 'Azure Firewall',
            'Azure Load Balancer', 'Azure Application Gateway', 'Azure Traffic Manager',
            'Azure Express Route', 'Azure VPN Gateway', 'Azure Content Delivery Network'
        ],
        'Monitor and Backup Azure resources': [
            'Azure Monitor'
        ],
        'Threat Protection': [
            'Azure Sentinel', 'Advanced Threat Protection',
            'Azure Information Protection', 'Azure DDoS Protection'
        ]
    }
    
    # Extract content for each topic
    def extract_topic_content(topic_name, full_content):
        """Extract detailed content for a topic"""
        lines = full_content.split('\n')
        start_idx = None
        end_idx = None
        
        for i, line in enumerate(lines):
            if line.strip().startswith(topic_name):
                start_idx = i
            if start_idx is not None and i > start_idx and (line.startswith('--Back to Index--') or (line and line[0].isupper() and i > start_idx + 1)):
                end_idx = i
                break
        
        if start_idx is not None:
            if end_idx is None:
                end_idx = min(start_idx + 30, len(lines))
            description = ' '.join([l.strip() for l in lines[start_idx+1:end_idx] if l.strip() and not l.startswith('●')])
            return description[:300].strip() if description else f'Learn about {topic_name}'
        return f'Learn about {topic_name}'
    
    # Build structured data
    structured_data = []
    for section_name in sections:
        section_data = {
            'name': section_name,
            'icon': get_icon_for_section(section_name),
            'topics': []
        }
        
        for topic in sections[section_name]:
            topic_data = {
                'name': topic,
                'icon': get_icon_for_topic(topic),
                'description': extract_topic_content(topic, content)
            }
            section_data['topics'].append(topic_data)
        
        structured_data.append(section_data)
    
    return structured_data

def get_icon_for_section(section_name):
    """Return emoji for sections"""
    icons = {
        'Azure Basics': '🔷',
        'Manage Azure Identities and Governance': '👤',
        'Implement and Manage Storage': '💾',
        'Deploy and Manage Azure Compute Resources': '⚙️',
        'Configure and Manage Virtual Networking': '🌐',
        'Monitor and Backup Azure resources': '📊',
        'Threat Protection': '🛡️'
    }
    return icons.get(section_name, '📘')

def get_icon_for_topic(topic_name):
    """Return emoji for topics"""
    icons = {
        'Azure Portal': '🔷',
        'Azure CLI': '💻',
        'Azure Powershell': '🔧',
        'Azure Resource Manager': '📦',
        'Azure Pricing': '💰',
        'Azure Security Centre': '🔒',
        'Azure Advisor': '💡',
        'Azure Active Directory': '👤',
        'Azure Role-Based Access Control': '🔑',
        'Azure Policy': '📋',
        'Azure Service Health': '❤️',
        'Azure Key Vault': '🔐',
        'Azure Blob service': '💾',
        'Azure File Storage': '📁',
        'Azure Disk Storage': '💿',
        'Azure Queue Storage': '📮',
        'Azure Table Storage': '📊',
        'Azure Archive Storage': '📦',
        'Azure Virtual Machine': '🖥️',
        'Azure App Service': '🚀',
        'Application Service Environments': '🏢',
        'Azure Container Registry': '📦',
        'Azure Container Instances': '🐳',
        'Azure Kubernetes Service': '☸️',
        'Azure Virtual Network': '🌐',
        'Azure DNS': '🔗',
        'Azure Firewall': '🔥',
        'Azure Load Balancer': '⚖️',
        'Azure Application Gateway': '🚪',
        'Azure Traffic Manager': '🚦',
        'Azure Express Route': '⚡',
        'Azure VPN Gateway': '🔌',
        'Azure Content Delivery Network': '📡',
        'Azure Monitor': '📊',
        'Azure Sentinel': '🛡️',
        'Advanced Threat Protection': '⚠️',
        'Azure Information Protection': '🏷️',
        'Azure DDoS Protection': '🛑'
    }
    return icons.get(topic_name, '📘')

# Load structured content
try:
    COURSE_DATA = parse_az_txt()
except Exception as e:
    print(f"Error parsing az.txt: {e}")
    COURSE_DATA = []

@app.route('/')
def home():
    """Home page showing all sections and topics"""
    return render_template('index.html', sections=COURSE_DATA)

@app.route('/section/<int:section_idx>')
def section(section_idx):
    """View a specific section with all its topics"""
    if section_idx < 0 or section_idx >= len(COURSE_DATA):
        return 'Section not found', 404
    
    section_data = COURSE_DATA[section_idx]
    return render_template('section.html', 
                          section=section_data,
                          section_idx=section_idx,
                          total_sections=len(COURSE_DATA))

@app.route('/topic/<int:section_idx>/<int:topic_idx>')
def topic(section_idx, topic_idx):
    """View detailed topic information"""
    if section_idx < 0 or section_idx >= len(COURSE_DATA):
        return 'Section not found', 404
    
    section = COURSE_DATA[section_idx]
    if topic_idx < 0 or topic_idx >= len(section['topics']):
        return 'Topic not found', 404
    
    topic_data = section['topics'][topic_idx]
    
    # Navigation
    prev_topic = None
    prev_section_idx = section_idx
    if topic_idx > 0:
        prev_topic = topic_idx - 1
    elif section_idx > 0:
        prev_section_idx = section_idx - 1
        prev_topic = len(COURSE_DATA[prev_section_idx]['topics']) - 1
    
    next_topic = None
    next_section_idx = section_idx
    if topic_idx < len(section['topics']) - 1:
        next_topic = topic_idx + 1
    elif section_idx < len(COURSE_DATA) - 1:
        next_section_idx = section_idx + 1
        next_topic = 0
    
    return render_template('topic.html',
                          topic=topic_data,
                          section=section,
                          section_idx=section_idx,
                          topic_idx=topic_idx,
                          prev_section_idx=prev_section_idx if prev_topic is not None else None,
                          prev_topic=prev_topic,
                          next_section_idx=next_section_idx if next_topic is not None else None,
                          next_topic=next_topic)

if __name__ == '__main__':
    app.run(debug=True)
