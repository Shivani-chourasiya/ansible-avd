!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## Core Interfaces

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>core_interfaces</samp>](## "core_interfaces") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;p2p_links</samp>](## "core_interfaces.p2p_links") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- as</samp>](## "core_interfaces.p2p_links.[].as") | List, items: String |  |  |  | AS Numbers for BGP | Required with bgp peering<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].as.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- node_a_as<br>- node_b_as |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP).<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses or Required with ip_pool.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links.[].include_in_underlay_protocol") | Boolean |  | True |  | Add this interface to underlay routing protocol.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured | Required unless using port-channels<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].interfaces.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- node_a_interface<br>- node_b_interface |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].ip.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links.[].ip_pool") | String |  |  |  | P2P Pool Name<br>IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links.[].isis_authentication_key") | String |  | $1c$sTNAlR6rKSw= |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links.[].isis_authentication_mode") | String |  | md5 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links.[].isis_circuit_type") | String |  | level-2 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links.[].isis_hello_padding") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links.[].isis_metric") | Integer |  | 60 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links.[].macsec_profile") | String |  |  |  | MAC Security Profile Name<br>MAC Security Profile<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links.[].mpls_ip") | Boolean |  |  |  | Default value is true if switch.mpls_lsr is true<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links.[].mpls_ldp") | Boolean |  |  |  | Default value is true for ldp underlay variants, otherwise false<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "core_interfaces.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].nodes.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- node_a<br>- node_b |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links.[].port_channel.mode") | String |  | active |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].node_interfaces") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].node_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "core_interfaces.p2p_links.[].profile") | String |  |  |  | P2P Profile Name<br>Profile defined under p2p_profiles<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp_enable</samp>](## "core_interfaces.p2p_links.[].ptp_enable") | Boolean |  | False |  | Enable PTP<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links.[].qos_profile") | String |  |  |  | QOS Profile Name<br>QOS Service Profile<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links.[].speed") | String |  |  | Valid Values:<br>- speed<br>- auto speed<br>- forced speed |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links.[].subnet") | String |  |  |  | Subnet used on this P2P link or Optional<br> |
| [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "core_interfaces.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_pool</samp>](## "core_interfaces.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "core_interfaces.p2p_links_ip_pools.[].name") | String |  |  |  | P2P Pool Name |
| [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "core_interfaces.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "core_interfaces.p2p_links_profiles.[].name") | String |  |  |  | P2P Profile Name<br>Any variable supported under p2p_links can be inherited from a profile.<br> |

### YAML

```yaml
core_interfaces:
  p2p_links:
    - as:
        - <str>
      bfd: <bool>
      id: <int>
      include_in_underlay_protocol: <bool>
      interfaces:
        - <str>
      ip:
        - <str>
      ip_pool: <str>
      ipv6_enable: <bool>
      isis_authentication_key: <str>
      isis_authentication_mode: <str>
      isis_circuit_type: <str>
      isis_hello_padding: <bool>
      isis_metric: <int>
      macsec_profile: <str>
      mpls_ip: <bool>
      mpls_ldp: <bool>
      mtu: <int>
      nodes:
        - <str>
      port_channel:
        mode: <str>
        nodes_child_interfaces:
          - node: <str>
            node_interfaces:
              - <str>
      profile: <str>
      ptp_enable: <bool>
      qos_profile: <str>
      raw_eos_cli: <str>
      speed: <str>
      subnet: <str>
  p2p_links_ip_pools:
    - ipv4_pool: <str>
      name: <str>
  p2p_links_profiles:
    - name: <str>
```

## Isis Default Circuit Type

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

### YAML

```yaml
isis_default_circuit_type: <str>
```

## Isis Default Metric

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | 50 |  |  |

### YAML

```yaml
isis_default_metric: <int>
```
