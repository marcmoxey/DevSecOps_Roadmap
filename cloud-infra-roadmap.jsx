import { useState } from "react";

// ─── DATA ────────────────────────────────────────────────────────────────────
// Structure: each stage is a BUILD MILESTONE on the home lab.
// Skills, resources, security, and resume bullets all attach to what you just built.

const stages = [
  {
    id: 1,
    emoji: "🔌",
    title: "Bring the server online",
    weeks: "3–4 weeks",
    tagline: "From a box on your desk to a server you control from anywhere.",
    color: "#4ade80",
    milestone: "By the end of this stage: your Beelink runs Ubuntu Server, has a fixed address on your network, a firewall, and you control it entirely from your PC over SSH — no monitor, no keyboard.",
    steps: [
      "Install Ubuntu Server 24.04 LTS on the Beelink (one-time, needs monitor + keyboard)",
      "Find its IP, SSH into it from your PC for the first time",
      "Give it a static IP with Netplan so the address never changes",
      "Set up ufw and only open what you need",
      "Do the TryHackMe Bash Scripting room — this is what ties your commands into a real script",
      "Write a bash script that checks disk usage hourly via cron, logs warnings over 80%",
    ],
    resources: [
      { label: "TryHackMe – Linux Fundamentals (1, 2, 3)", url: "https://tryhackme.com/module/linux-fundamentals", tag: "THM sub" },
      { label: "TryHackMe – Pre-Security Path", url: "https://tryhackme.com/path/outline/presecurity", tag: "THM sub" },
      { label: "TryHackMe – Networking Fundamentals", url: "https://tryhackme.com/module/networking-fundamentals", tag: "THM sub" },
      { label: "TryHackMe – Bash Scripting", url: "https://tryhackme.com/room/bashscripting", tag: "THM sub" },
      { label: "The Linux Command Line – free book", url: "https://linuxcommand.org/tlcl.php", tag: "free" },
      { label: "Ubuntu Server 24.04 LTS", url: "https://ubuntu.com/download/server", tag: "download" },
      { label: "Ubuntu – Static IP with Netplan", url: "https://ubuntu.com/server/docs/network-configuration", tag: "official" },
      { label: "ShellCheck – lint your bash scripts", url: "https://www.shellcheck.net/", tag: "tool" },
    ],
    note: "Do TryHackMe first, then apply the same commands on your real Beelink the same day. THM is the safe sandbox; the Beelink is where it becomes real. The Bash Scripting room directly unblocks the disk-check script below — do it right before writing that script.",
    secNote: "A world-readable config file or an open port is exactly what DevSecOps work fixes later. Note which ports ufw blocks by default — you'll explain this in interviews.",
    journal: "First SSH connection — the exact command, the IP, any errors. Every command that confused you and what it actually does. Run your script through shellcheck.net and note what it flags.",
    skills: ["Linux CLI", "SSH", "Bash scripting", "Networking basics", "File permissions", "ufw", "Netplan", "cron"],
  },
  {
    id: 2,
    emoji: "🐍",
    title: "Write a tool that watches the server",
    weeks: "3–4 weeks",
    tagline: "Stop SSHing in manually to check on things — write something that does it for you.",
    color: "#60a5fa",
    milestone: "By the end of this stage: a Python CLI on your PC that connects to your Beelink over SSH and reports disk, memory, and uptime — a real tool you'll keep using for the rest of the roadmap.",
    steps: [
      "Learn Python basics — variables, loops, functions, files (Automate the Boring Stuff ch. 1-10, 3rd edition)",
      "Do the TryHackMe Regular Expressions room, then AtBS chapter 9 (regex) back to back — same concept, two syntaxes",
      "Learn CLI program design (ch. 12) — directly feeds the labcheck tool build",
      "Learn JSON/CSV handling (ch. 18) — this is how almost every tool below talks",
      "Learn subprocess/scheduling basics (ch. 19)",
      "Use Paramiko to connect from your PC to your Beelink over SSH from Python",
      "Wrap it in a CLI with argparse or click — `labcheck --host beelink`",
      "Output disk/memory/uptime as a clean report",
    ],
    resources: [
      { label: "Python official tutorial", url: "https://docs.python.org/3/tutorial/", tag: "official" },
      { label: "Automate the Boring Stuff 3rd edition (free)", url: "https://automatetheboringstuff.com/", tag: "free" },
      { label: "AtBS – Ch. 1-5 (Basics, Flow Control, Loops, Functions, Debugging)", url: "https://automatetheboringstuff.com/", tag: "free" },
      { label: "AtBS – Ch. 6-10 (Lists, Dicts, Strings, Regex, Files)", url: "https://automatetheboringstuff.com/", tag: "free" },
      { label: "AtBS – Ch. 12 (CLI Programs — feeds the labcheck build)", url: "https://automatetheboringstuff.com/", tag: "free" },
      { label: "TryHackMe – Regular Expressions (pair with ch. 9)", url: "https://tryhackme.com/room/catregex", tag: "THM sub" },
      { label: "AtBS – Ch. 18 (CSV, JSON, and XML)", url: "https://automatetheboringstuff.com/", tag: "free" },
      { label: "AtBS – Ch. 19 (Scheduling, subprocess)", url: "https://automatetheboringstuff.com/", tag: "free" },
      { label: "Real Python – Working with JSON", url: "https://realpython.com/python-json/", tag: "free" },
      { label: "Real Python – subprocess module", url: "https://realpython.com/python-subprocess/", tag: "free" },
      { label: "Paramiko – SSH from Python", url: "https://www.paramiko.org/", tag: "library" },
      { label: "TechWorld with Nana – Python Full Course", url: "https://www.youtube.com/watch?v=t8pPdKYpowI", tag: "video" },
    ],
    note: "Skip AtBS chapters 11, 13-17, 20-24 — those are desktop/office/GUI automation, not relevant here. Do the TryHackMe Regex room and ch. 9 close together — seeing the same pattern syntax in both makes both stick better. Ch. 12 (CLI Programs) is new in the 3rd edition and directly feeds the labcheck build — don't skip it.",
    secNote: null,
    journal: "Note every Python concept that feels different from bash. Compare parsing command output in Python vs awk/grep — you'll use both, for different jobs.",
    skills: ["Python", "Scripting & automation", "argparse / click", "Regex", "JSON", "Paramiko (SSH)", "Error handling"],
  },
  {
    id: 3,
    emoji: "☁️",
    title: "Stand up the same thing in AWS",
    weeks: "4–5 weeks",
    tagline: "Take what runs on your Beelink and run it in the cloud too.",
    color: "#fb923c",
    milestone: "By the end of this stage: a simple app running on EC2 behind a load balancer, files in S3, and a Python script using Boto3 that audits your AWS account for security issues — like your Beelink, but in the cloud.",
    steps: [
      "Sign up for AWS Free Tier",
      "Launch an EC2 instance — SSH into it exactly like your Beelink",
      "Deploy a simple web app, put it behind a load balancer",
      "Create an S3 bucket, upload/download files via CLI",
      "Set up IAM users/roles — start from zero permissions, add only what's needed",
      "Write a Boto3 script that lists EC2 instances and S3 buckets, and flags any public bucket",
    ],
    resources: [
      { label: "AWS Free Tier – sign up", url: "https://aws.amazon.com/free/", tag: "free" },
      { label: "FreeCodeCamp – AWS Full Course", url: "https://www.youtube.com/watch?v=NhDYbskXRgc", tag: "video" },
      { label: "AWS CLI docs", url: "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html", tag: "official" },
      { label: "Boto3 – AWS SDK for Python", url: "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html", tag: "official" },
      { label: "AWS Well-Architected Framework", url: "https://aws.amazon.com/architecture/well-architected/", tag: "official" },
      { label: "AWS Well-Architected — Security Pillar", url: "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html", tag: "official" },
    ],
    note: "Everything you build in this stage feeds directly into your AWS Solutions Architect Associate (SAA-C03) certification later — EC2, S3, VPC, IAM, and load balancers are core exam topics. Hands-on experience here makes studying for SAA much faster than starting cold.",
    secNote: "IAM is the security model. Start every task with zero permissions and add only what's needed — the opposite of how most people learn it. The Boto3 script that flags public S3 buckets is a real security automation task, not a toy example.",
    govtech: "AWS GovCloud is the same services with stricter compliance (FedRAMP, ITAR). The console looks the same, Boto3 calls are the same — read the GovCloud overview once so it's familiar in interviews.",
    journal: "Every IAM permission error — what you were trying to do, what policy fixed it. What each service costs, so cost awareness becomes automatic.",
    skills: ["EC2", "S3", "VPC", "IAM", "Load Balancers", "AWS CLI", "Boto3"],
  },
  {
    id: 4,
    emoji: "🏗️",
    title: "Rebuild it all as code",
    weeks: "2–3 weeks",
    tagline: "Delete everything in AWS. Bring it all back with one command.",
    color: "#a78bfa",
    milestone: "By the end of this stage: everything from Stage 3 (EC2, S3, VPC, load balancer) exists as Terraform code. You can destroy it and rebuild it identically — and a scanner checks it for misconfigurations before it ever deploys.",
    steps: [
      "Install Terraform, write your first resource block",
      "Recreate your EC2 + S3 + VPC + load balancer setup as .tf files",
      "terraform plan, apply, then destroy and apply again — confirm it's identical",
      "Run Checkov or tfsec against your code, fix every finding",
      "Start Security+ (SY0-701) study now — runs in parallel with this stage through Stage 5",
      "Study with Professor Messer's free videos (professormesser.com) as primary resource",
      "Use 'Get Certified Get Ahead' book (Darril Gibson) for reinforcement + 300+ built-in practice questions",
      "Supplement with Jason Dion's SY0-701 Practice Exams Set 1 (Udemy, ~$15) for extra volume closer to exam day",
    ],
    resources: [
      { label: "Terraform – Official AWS Getting Started", url: "https://developer.hashicorp.com/terraform/tutorials/aws-get-started", tag: "official" },
      { label: "Terraform AWS Provider docs", url: "https://registry.terraform.io/providers/hashicorp/aws/latest/docs", tag: "official" },
      { label: "TechWorld with Nana – Terraform Course", url: "https://www.youtube.com/watch?v=7xngnjfIlK4", tag: "video" },
      { label: "Terraform Associate Cert prep", url: "https://developer.hashicorp.com/terraform/tutorials/certification-003", tag: "cert" },
      { label: "Checkov – IaC security scanner", url: "https://www.checkov.io/", tag: "tool" },
      { label: "tfsec / Trivy config scanning", url: "https://aquasecurity.github.io/trivy/latest/docs/scanner/misconfiguration/", tag: "tool" },
      { label: "CompTIA Security+ (SY0-701) — exam page", url: "https://www.comptia.org/certifications/security", tag: "cert" },
      { label: "Professor Messer – Security+ SY0-701 (FREE videos)", url: "https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/", tag: "free" },
      { label: "Professor Messer – Free SY0-701 Practice Exam", url: "https://www.professormesser.com/sy0-701-success-bundle/", tag: "free" },
      { label: "Get Certified Get Ahead – Darril Gibson (book)", url: "https://www.amazon.com/CompTIA-Security-Study-Guide-SY0-701/dp/1394211066", tag: "paid" },
      { label: "Jason Dion – SY0-701 Practice Exams Set 1 (Udemy)", url: "https://www.udemy.com/course/comptia-security-practice-exams/", tag: "paid" },
      { label: "CompTIA – Official SY0-701 sample questions (free)", url: "https://www.comptia.org/training/resources/practice-tests", tag: "free" },
    ],
    note: "Security+ study runs in parallel with Terraform work — don't block one on the other. Aim to sit the Security+ exam by the end of Stage 5.",
    secNote: "Every Checkov/tfsec finding is exactly the kind of thing DevSecOps engineers triage daily. Treat each one as a mini case study, not just a checkbox to clear.",
    govtech: "Security+ is a hard requirement under DoD 8570/8140 for most govtech roles — getting it done here means you can apply with it already on your resume when Stage 5-6 completes.",
    journal: "State file mistakes — everyone destroys something by accident. The commands that saved you: plan, import, state list, state rm. Every Checkov/tfsec finding and how you fixed it.",
    skills: ["Terraform", "IaC", "State management", "Modules", "HCL", "IaC security scanning"],
  },
  {
    id: 5,
    emoji: "🐳",
    title: "Move everything into containers — on the Beelink",
    weeks: "5–6 weeks",
    tagline: "Your home lab becomes a small Kubernetes cluster.",
    color: "#22d3ee",
    milestone: "By the end of this stage: your Beelink runs k3s (lightweight Kubernetes). Your Python tool from Stage 2 runs as a pod, with security policies enforced — nothing runs as root, and a policy engine blocks anything that tries.",
    steps: [
      "Install Docker on the Beelink — run a throwaway/sample service in it for practice (real Jellyfin/Nextcloud/Vaultwarden live on the NAS via TrueNAS instead, kept separate from this lab)",
      "Write a Dockerfile for your Python tool from Stage 2",
      "Scan the image with Trivy, fix what it flags (base image, versions)",
      "Install k3s on the Beelink",
      "Write Kubernetes manifests for your app — Deployment, Service, Ingress",
      "Apply Pod Security Standards — non-root, no privilege escalation",
      "Install OPA Gatekeeper, write a policy that blocks any pod running as root — test that it actually blocks one",
      "Open the app in your PC browser via the Ingress",
    ],
    resources: [
      { label: "Docker – Official Getting Started", url: "https://docs.docker.com/get-started/", tag: "official" },
      { label: "TechWorld with Nana – Docker Crash Course", url: "https://www.youtube.com/watch?v=3c-iBn73dDE", tag: "video" },
      { label: "KodeKloud – Kubernetes for Beginners", url: "https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on/", tag: "free" },
      { label: "TechWorld with Nana – Kubernetes Full Course", url: "https://www.youtube.com/watch?v=X48VuDVv0do", tag: "video" },
      { label: "k3s – Kubernetes for home servers", url: "https://k3s.io/", tag: "tool" },
      { label: "Kubernetes official docs", url: "https://kubernetes.io/docs/home/", tag: "official" },
      { label: "Techno Tim – k3s homelab setup", url: "https://www.youtube.com/@TechnoTim", tag: "video" },
      { label: "Trivy – container image scanning", url: "https://aquasecurity.github.io/trivy/", tag: "tool" },
      { label: "Kubernetes – Pod Security Standards", url: "https://kubernetes.io/docs/concepts/security/pod-security-standards/", tag: "official" },
      { label: "OPA Gatekeeper – policy as code", url: "https://open-policy-agent.github.io/gatekeeper/website/docs/", tag: "tool" },
      { label: "CKA exam curriculum", url: "https://github.com/cncf/curriculum", tag: "cert" },
      { label: "── AWS SAA STUDY (start after Security+ exam) ──", url: "#", tag: "cert" },
      { label: "Stephane Maarek – Ultimate AWS SAA-C03 Course (Udemy, ~$15 on sale)", url: "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/", tag: "paid" },
      { label: "Tutorials Dojo – SAA-C03 Practice Exams (Jon Bonso, 401 questions)", url: "https://portal.tutorialsdojo.com/courses/aws-certified-solutions-architect-associate-practice-exams/", tag: "paid" },
      { label: "Tutorials Dojo – Free AWS Cheat Sheets", url: "https://tutorialsdojo.com/aws-cheat-sheets/", tag: "free" },
      { label: "AWS Official Practice Question Set (free, ~20 questions from AWS)", url: "https://aws.amazon.com/certification/certified-solutions-architect-associate/", tag: "free" },
      { label: "AWS Skill Builder – free labs and digital courses", url: "https://skillbuilder.aws/", tag: "free" },
    ],
    note: "Two things running in parallel this stage: the k3s/Kubernetes build AND AWS SAA study (once Security+ exam is done). Your Stage 3-4 AWS hands-on means ~40-50% of SAA content is already familiar — you're filling gaps, not starting cold. Aim to sit SAA after Stage 6.",
    secNote: "This is the heart of the DevSecOps story: image scanning + policy enforcement, on a cluster you run and can demonstrate live. 'I wrote a policy and tested that it blocks a real violation' is a strong interview line.",
    govtech: "Sit the Security+ exam at the START of this stage if you haven't already — once passed, you can start applying while continuing the roadmap. AWS SAA study runs in the background of this stage, sits the exam around Stage 6-7.",
    journal: "Every Trivy finding and fix. Pod Security Standard violations and how you resolved them. Your Gatekeeper policy in plain English. Deployment vs Service vs Ingress, in your own words.",
    skills: ["Docker", "Kubernetes", "k3s", "Deployments", "Services", "Ingress", "ConfigMaps", "Image scanning (Trivy)", "Pod Security Standards", "Policy as code (OPA)"],
  },
  {
    id: 6,
    emoji: "⚙️",
    title: "Make the cluster update itself",
    weeks: "2–3 weeks",
    tagline: "Push code on your PC. Watch your Beelink redeploy itself automatically.",
    color: "#f472b6",
    milestone: "By the end of this stage: a GitHub Actions pipeline tests, scans, and builds your app, and ArgoCD running on your Beelink's k3s automatically deploys it. The pipeline refuses to ship anything with a critical vulnerability.",
    steps: [
      "Push your app's code (from Stage 5) to a GitHub repo",
      "Write a GitHub Actions workflow: test → Trivy scan image → Checkov scan Terraform → build → push to Docker Hub",
      "Make the pipeline fail the build on a critical Trivy finding — verify it actually does, on purpose",
      "Install ArgoCD on your Beelink's k3s",
      "Point ArgoCD at your repo, make a commit, watch it deploy automatically",
      "Enable Dependabot on the repo",
    ],
    resources: [
      { label: "GitHub Actions – Official Docs", url: "https://docs.github.com/en/actions", tag: "official" },
      { label: "ArgoCD – Getting Started", url: "https://argo-cd.readthedocs.io/en/stable/getting_started/", tag: "official" },
      { label: "TechWorld with Nana – CI/CD Full Course", url: "https://www.youtube.com/watch?v=R8_veQiYBjI", tag: "video" },
      { label: "GitHub – Dependabot", url: "https://docs.github.com/en/code-security/dependabot", tag: "official" },
      { label: "Trivy GitHub Action", url: "https://github.com/aquasecurity/trivy-action", tag: "tool" },
    ],
    note: null,
    secNote: "A pipeline that fails the build on a critical CVE — and that you can show actually failing on purpose — is one of the single strongest things to demo in an interview. Security inside the pipeline, not bolted on after.",
    journal: "Every pipeline failure — what stage broke, the error, the fix. Specifically, the time the security scan stage failed and how you resolved it. How you store secrets in GitHub Actions safely.",
    skills: ["GitHub Actions", "ArgoCD", "GitOps", "Docker Hub", "Pipeline debugging", "Secret management", "Security gates in CI/CD", "Dependabot"],
  },
  {
    id: 7,
    emoji: "📊",
    title: "Make the lab tell you when something's wrong",
    weeks: "2–3 weeks",
    tagline: "Stop checking on it. Let it alert you.",
    color: "#fb923c",
    milestone: "By the end of this stage: Grafana dashboards on your PC browser show your Beelink's health in real time, an alert fires if memory goes over 80%, and Falco is watching the cluster for suspicious activity — and you've seen it catch something.",
    steps: [
      "Run Prometheus and Grafana as containers on the Beelink",
      "Instrument your Python app (from Stage 2/5) with Prometheus metrics",
      "Build a Grafana dashboard — CPU, RAM, disk, network",
      "Set an alert: fires when memory > 80%",
      "Install Falco on the k3s cluster",
      "Deliberately trigger a default Falco rule (e.g. shell into a running container) and capture the alert",
    ],
    resources: [
      { label: "Prometheus – Getting Started", url: "https://prometheus.io/docs/prometheus/latest/getting_started/", tag: "official" },
      { label: "Grafana – Official Docs", url: "https://grafana.com/docs/grafana/latest/", tag: "official" },
      { label: "Prometheus Python client library", url: "https://github.com/prometheus/client_python", tag: "library" },
      { label: "TechWorld with Nana – Prometheus & Grafana", url: "https://www.youtube.com/watch?v=QoDqxm7ybLc", tag: "video" },
      { label: "Falco – runtime security monitoring", url: "https://falco.org/docs/", tag: "tool" },
    ],
    note: null,
    secNote: null,
    journal: "What metrics you track and why. Your alerting rules in plain English. The Falco alert you triggered and what it told you. Screenshots of Grafana and the Falco alert — portfolio gold.",
    skills: ["Prometheus", "Grafana", "Alerting", "Loki", "Python instrumentation", "Runtime security monitoring (Falco)"],
  },
  {
    id: 8,
    emoji: "🔒",
    title: "Audit the whole lab — then tell its story",
    weeks: "3–4 weeks",
    tagline: "Treat your home lab like a production system getting a security review.",
    color: "#f87171",
    milestone: "By the end of this stage: every part of your lab — Beelink, AWS, Terraform, Kubernetes — has been audited and hardened, with a documented before/after. Your journal is cleaned up into a public GitHub portfolio.",
    steps: [
      "Pick 5-8 specific TryHackMe rooms (not full paths) covering container security, IaC security, OWASP Top 10, and Linux privilege escalation",
      "Audit your Beelink: disable root SSH login, key-based auth only, review open ports, Docker permissions",
      "Audit your NAS (real services): confirm Vaultwarden is Tailscale-only, ZFS encryption enabled on Nextcloud dataset, no default passwords remaining",
      "Audit AWS IAM roles — remove every permission not actually used, enable CloudTrail",
      "Re-run Checkov, Trivy, and tfsec across everything from Stages 3-6, fix remaining findings",
      "Write up the full before/after for each",
      "Clean up your journal into a public GitHub repo",
      "Write a README for each project: what it does, why you built it, how to run it",
    ],
    resources: [
      { label: "TryHackMe – DevSecOps Path (browse for rooms)", url: "https://tryhackme.com/path/outline/devsecops", tag: "THM sub" },
      { label: "TryHackMe – Jr Penetration Tester Path (browse for rooms)", url: "https://tryhackme.com/path/outline/jrpenetrationtester", tag: "THM sub" },
      { label: "AWS IAM Best Practices", url: "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html", tag: "official" },
      { label: "OWASP Top 10", url: "https://owasp.org/www-project-top-ten/", tag: "free" },
      { label: "CIS Benchmarks", url: "https://www.cisecurity.org/cis-benchmarks", tag: "free" },
    ],
    note: "Don't do the full DevSecOps or Jr Pentester paths — together that's 100+ hours, much of it overlapping with what your lab already covers hands-on. Browse each path's room list and cherry-pick just: container security, IaC security, OWASP Top 10, and Linux privilege escalation. That's 5-8 rooms, a few days to two weeks. Spend the time saved on the actual audit work below — auditing your real setup is more valuable than completing more rooms.",
    secNote: null,
    journal: "This stage doesn't add a new journal habit — it's where the previous 7 stages' journals become your portfolio. Emphasize the security scans and fixes throughout every README.",
    skills: ["IAM least privilege", "SSH hardening", "CloudTrail", "CIS Benchmarks", "Vulnerability remediation", "Portfolio", "GitHub"],
  },
];

const tagColors = {
  "THM sub": { bg: "#1e3a5f", text: "#60a5fa" },
  "free": { bg: "#14532d", text: "#4ade80" },
  "official": { bg: "#1c1917", text: "#a8a29e" },
  "video": { bg: "#3b0764", text: "#c084fc" },
  "library": { bg: "#1e3a5f", text: "#60a5fa" },
  "download": { bg: "#14532d", text: "#4ade80" },
  "tool": { bg: "#7f1d1d", text: "#fca5a5" },
  "cert": { bg: "#7c2d12", text: "#fb923c" },
};

// ─── COMPONENT ───────────────────────────────────────────────────────────────

export default function Roadmap() {
  const [open, setOpen] = useState(null);
  const [tab, setTab] = useState("lab");

  return (
    <div style={{
      fontFamily: "'Inter', system-ui, -apple-system, sans-serif",
      background: "#0c0c0e",
      minHeight: "100vh",
      color: "#d4d4d8",
    }}>

      {/* ── HERO ── */}
      <div style={{
        padding: "48px 24px 40px",
        borderBottom: "1px solid #1f1f23",
        maxWidth: 720,
        margin: "0 auto",
      }}>
        <p style={{ fontSize: 12, letterSpacing: "0.12em", color: "#71717a", textTransform: "uppercase", marginBottom: 16, fontWeight: 500 }}>
          Your home lab, stage by stage
        </p>
        <h1 style={{ fontSize: 32, fontWeight: 700, color: "#fafafa", margin: "0 0 12px", lineHeight: 1.15 }}>
          One Beelink.<br />
          <span style={{ color: "#4ade80" }}>Eight builds. Job-ready.</span>
        </h1>
        <p style={{ fontSize: 15, color: "#71717a", margin: "0 0 28px", lineHeight: 1.6, maxWidth: 480 }}>
          Every stage adds something real to your home server. By the end it's a small, secured Kubernetes platform you built, broke, fixed, and can talk about in interviews — ~9 months at 2–3 hrs/day.
        </p>

        {/* stat pills */}
        <div style={{ display: "flex", flexWrap: "wrap", gap: 10, marginBottom: 32 }}>
          {[
            { icon: "🖥️", label: "Your Beelink is the lab" },
            { icon: "💻", label: "SSH in from your PC" },
            { icon: "📓", label: "Journal every stage" },
            { icon: "🔴", label: "TryHackMe sub used" },
            { icon: "🐍", label: "Python, not Go" },
            { icon: "🔒", label: "Security built in, not bolted on" },
          ].map((p, i) => (
            <div key={i} style={{
              display: "flex", alignItems: "center", gap: 8,
              padding: "7px 14px", background: "#18181b",
              border: "1px solid #27272a", borderRadius: 8,
              fontSize: 13, color: "#a1a1aa",
            }}>
              <span>{p.icon}</span>
              <span>{p.label}</span>
            </div>
          ))}
        </div>

        {/* tabs */}
        <div style={{ display: "flex", gap: 4, background: "#18181b", padding: 4, borderRadius: 10, width: "fit-content", flexWrap: "wrap" }}>
          {[
            { id: "lab", label: "The Lab Build" },
            { id: "setup", label: "Getting Started" },
            { id: "journal", label: "Journaling" },
            { id: "jobs", label: "Getting Hired" },
            { id: "govtech", label: "Govtech" },
          ].map(t => (
            <button key={t.id} onClick={() => setTab(t.id)} style={{
              padding: "7px 16px", borderRadius: 7, border: "none", cursor: "pointer",
              fontSize: 13, fontWeight: 500,
              background: tab === t.id ? "#fafafa" : "transparent",
              color: tab === t.id ? "#0c0c0e" : "#71717a",
              transition: "all 0.15s",
            }}>{t.label}</button>
          ))}
        </div>
      </div>

      {/* ── CONTENT ── */}
      <div style={{ maxWidth: 720, margin: "0 auto", padding: "32px 24px 64px" }}>

        {/* LAB BUILD */}
        {tab === "lab" && (
          <div>
            {/* progress line */}
            <div style={{ display: "flex", gap: 4, marginBottom: 24 }}>
              {stages.map(s => (
                <div key={s.id} style={{ flex: 1, height: 4, borderRadius: 2, background: s.color + "44" }} />
              ))}
            </div>

            <div style={{
              background: "#18181b", border: "1px solid #27272a",
              borderLeft: "3px solid #4ade80",
              borderRadius: 8, padding: "14px 18px",
              marginBottom: 24, fontSize: 13, color: "#a1a1aa", lineHeight: 1.7,
            }}>
              <span style={{ color: "#4ade80", fontWeight: 600 }}>🖥️ One server, building the whole way through. </span>
              Each stage below adds something new to the same Beelink — by Stage 8 it's running Kubernetes with security scanning, policy enforcement, CI/CD, and monitoring, all of which you built and can explain.
            </div>

            {stages.map((stage) => {
              const isOpen = open === stage.id;
              return (
                <div key={stage.id} style={{ marginBottom: 8 }}>
                  <button
                    onClick={() => setOpen(isOpen ? null : stage.id)}
                    style={{
                      width: "100%", textAlign: "left",
                      background: isOpen ? "#18181b" : "#111113",
                      border: `1px solid ${isOpen ? stage.color + "55" : "#27272a"}`,
                      borderRadius: isOpen ? "10px 10px 0 0" : 10,
                      padding: "16px 18px",
                      cursor: "pointer",
                      display: "flex", alignItems: "center", gap: 14,
                      transition: "border-color 0.15s",
                    }}
                  >
                    <span style={{
                      width: 32, height: 32, borderRadius: "50%", flexShrink: 0,
                      background: stage.color + "1f", border: `1px solid ${stage.color}55`,
                      display: "flex", alignItems: "center", justifyContent: "center",
                      fontSize: 16,
                    }}>{stage.emoji}</span>
                    <div style={{ flex: 1 }}>
                      <div style={{ display: "flex", alignItems: "baseline", gap: 10, flexWrap: "wrap" }}>
                        <span style={{ fontSize: 11, color: "#52525b", fontWeight: 600 }}>STAGE {stage.id}</span>
                        <span style={{ fontWeight: 600, fontSize: 15, color: "#fafafa" }}>{stage.title}</span>
                        <span style={{ fontSize: 12, color: "#52525b" }}>{stage.weeks}</span>
                      </div>
                      <div style={{ fontSize: 13, color: "#52525b", marginTop: 2 }}>{stage.tagline}</div>
                    </div>
                    <span style={{
                      width: 24, height: 24, borderRadius: "50%",
                      background: isOpen ? stage.color + "22" : "#1f1f23",
                      color: isOpen ? stage.color : "#52525b",
                      display: "flex", alignItems: "center", justifyContent: "center",
                      fontSize: 16, flexShrink: 0, fontWeight: 300,
                    }}>{isOpen ? "−" : "+"}</span>
                  </button>

                  {isOpen && (
                    <div style={{
                      background: "#18181b",
                      border: `1px solid ${stage.color}55`,
                      borderTop: "none",
                      borderRadius: "0 0 10px 10px",
                      padding: "20px 18px",
                    }}>
                      {/* milestone */}
                      <div style={{
                        marginBottom: 18, padding: "12px 14px", borderRadius: 8,
                        background: stage.color + "11", border: `1px solid ${stage.color}33`,
                      }}>
                        <div style={{ fontSize: 11, color: stage.color, fontWeight: 600, letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: 6 }}>
                          🎯 What your lab looks like after this stage
                        </div>
                        <div style={{ fontSize: 13, color: "#cbd5e1", lineHeight: 1.7 }}>{stage.milestone}</div>
                      </div>

                      {/* steps */}
                      <div style={{ marginBottom: 18 }}>
                        <SectionLabel color={stage.color}>Build it — step by step</SectionLabel>
                        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                          {stage.steps.map((step, i) => (
                            <div key={i} style={{ display: "flex", gap: 10, fontSize: 13, color: "#a1a1aa", lineHeight: 1.6 }}>
                              <span style={{
                                flexShrink: 0, width: 20, height: 20, borderRadius: "50%",
                                background: "#111113", border: `1px solid ${stage.color}55`, color: stage.color,
                                fontSize: 11, fontWeight: 600,
                                display: "flex", alignItems: "center", justifyContent: "center", marginTop: 1,
                              }}>{i + 1}</span>
                              <span>{step}</span>
                            </div>
                          ))}
                        </div>
                      </div>

                      {/* note */}
                      {stage.note && (
                        <Section color="#60a5fa" icon="💡" label="Note">
                          {stage.note}
                        </Section>
                      )}

                      {/* security lens */}
                      {stage.secNote && (
                        <Section color="#f87171" icon="🔒" label="Security lens">
                          {stage.secNote}
                        </Section>
                      )}

                      {/* govtech */}
                      {stage.govtech && (
                        <Section color="#facc15" icon="🇺🇸" label="Govtech track">
                          {stage.govtech}
                        </Section>
                      )}

                      {/* resources */}
                      <div style={{ marginBottom: 18 }}>
                        <SectionLabel color={stage.color}>Resources</SectionLabel>
                        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                          {stage.resources.map((r, i) => {
                            const tc = tagColors[r.tag] || { bg: "#27272a", text: "#a1a1aa" };
                            return (
                              <a key={i} href={r.url} target="_blank" rel="noopener noreferrer" style={{
                                display: "flex", alignItems: "center", gap: 10,
                                padding: "10px 14px", background: "#111113",
                                border: "1px solid #27272a", borderRadius: 8,
                                textDecoration: "none", color: "#d4d4d8", fontSize: 13,
                              }}>
                                <span style={{ flex: 1 }}>{r.label}</span>
                                <span style={{
                                  padding: "2px 8px", borderRadius: 4, fontSize: 11, fontWeight: 500,
                                  background: tc.bg, color: tc.text,
                                }}>{r.tag}</span>
                                <span style={{ color: "#3f3f46", fontSize: 12 }}>↗</span>
                              </a>
                            );
                          })}
                        </div>
                      </div>

                      {/* journal */}
                      <Section color="#facc15" icon="📓" label="Write in your journal">
                        {stage.journal}
                      </Section>

                      {/* skills */}
                      <div>
                        <SectionLabel color={stage.color}>Skills unlocked this stage</SectionLabel>
                        <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
                          {stage.skills.map((s, i) => (
                            <span key={i} style={{
                              padding: "4px 10px", background: "#111113",
                              border: "1px solid #27272a", borderRadius: 6,
                              fontSize: 12, color: "#71717a",
                            }}>{s}</span>
                          ))}
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}

        {/* GETTING STARTED */}
        {tab === "setup" && (
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            <InfoCard title="Your PC — where you work" icon="💻" color="#60a5fa">
              Your main machine. This is where you write code, watch tutorials, read docs, and open your terminal to SSH into your Beelink. You never need to sit in front of your server.
            </InfoCard>
            <InfoCard title="Your Beelink — the lab itself" icon="🖥️" color="#4ade80">
              Install Ubuntu Server on it. After first setup, unplug the monitor and keyboard — you control it entirely over SSH from your PC. Every stage above builds directly on this one machine. Breaking and fixing real hardware teaches more than any tutorial.
              <br /><br />
              <a href="https://ubuntu.com/download/server" target="_blank" rel="noopener noreferrer" style={{ color: "#4ade80" }}>Download Ubuntu Server 24.04 LTS →</a>
            </InfoCard>
            <InfoCard title="How SSH works day to day" icon="🔗" color="#a78bfa">
              <code style={{ background: "#111113", padding: "8px 12px", borderRadius: 6, display: "block", fontSize: 13, color: "#c084fc", marginTop: 8, lineHeight: 1.8 }}>
                # From your PC terminal{"\n"}
                ssh yourname@192.168.x.x{"\n"}
                {"\n"}
                # Now you're inside your Beelink{"\n"}
                # Install Docker, run containers, edit configs
              </code>
            </InfoCard>
            <InfoCard title="Why Python instead of Go" icon="🐍" color="#60a5fa">
              Most Junior DevOps/DevSecOps postings ask for <strong style={{ color: "#fafafa" }}>scripting ability</strong> — usually Python or Bash, rarely Go. Python is also the language behind most security automation: Boto3 for AWS, Paramiko for SSH.
              <br /><br />
              It's faster to get productive in — useful scripts within days, not weeks. If you move toward Platform Engineering later, Go becomes relevant (Kubernetes, Terraform are written in it) — but that's a future second language, not a blocker now.
            </InfoCard>
            <InfoCard title="TryHackMe — your security classroom" icon="🔴" color="#f87171">
              Covers Stage 1 (Linux Fundamentals, Pre-Security, Networking) and Stage 8 (DevSecOps, Jr Penetration Tester paths). Use it actively — spin up machines and do the tasks, then repeat on your real Beelink the same day.
              <br /><br />
              <a href="https://tryhackme.com" target="_blank" rel="noopener noreferrer" style={{ color: "#f87171" }}>Open TryHackMe →</a>
            </InfoCard>
            <InfoCard title="The security toolbelt" icon="🛠️" color="#fb923c">
              Free tools that run on your Beelink throughout the build, not saved for the end:
              <br /><br />
              • <strong style={{ color: "#fafafa" }}>Trivy</strong> — scans container images and IaC for vulnerabilities<br />
              • <strong style={{ color: "#fafafa" }}>Checkov / tfsec</strong> — scans Terraform for misconfigurations<br />
              • <strong style={{ color: "#fafafa" }}>OPA Gatekeeper</strong> — enforces policy in Kubernetes<br />
              • <strong style={{ color: "#fafafa" }}>Falco</strong> — detects suspicious runtime behavior<br />
              • <strong style={{ color: "#fafafa" }}>Dependabot</strong> — flags outdated/vulnerable dependencies
            </InfoCard>
            <InfoCard title="YouTube — use sparingly" icon="📺" color="#a78bfa">
              When a concept isn't clicking from docs alone, watch one video then go build it immediately. Two channels cover almost everything:
              <br /><br />
              • <a href="https://www.youtube.com/@TechWorldwithNana" target="_blank" rel="noopener noreferrer" style={{ color: "#a78bfa" }}>TechWorld with Nana</a> — Docker, K8s, CI/CD, Python
              <br />• <a href="https://www.youtube.com/@TechnoTim" target="_blank" rel="noopener noreferrer" style={{ color: "#a78bfa" }}>Techno Tim</a> — k3s and homelab on real hardware
            </InfoCard>
          </div>
        )}

        {/* JOURNAL */}
        {tab === "journal" && (
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            <InfoCard title="Why you journal everything" icon="📓" color="#facc15">
              Interviews constantly ask "tell me about a time you had to debug X" or "tell me about a vulnerability you found and fixed." Your journal is the answer. You will forget how you fixed things three months later. Writing it out forces you to actually understand what you did.
            </InfoCard>
            <InfoCard title="What to write each session" icon="✍️" color="#4ade80">
              <code style={{ background: "#111113", padding: "10px 14px", borderRadius: 6, display: "block", fontSize: 12, color: "#4ade80", lineHeight: 2 }}>
                Date: what you were working on{"\n"}
                Tried: what you attempted{"\n"}
                Problem: the exact error / finding{"\n"}
                Fix: what actually solved it{"\n"}
                Learned: one sentence takeaway
              </code>
            </InfoCard>
            <InfoCard title="Security findings get their own log" icon="🔍" color="#f87171">
              A running list of every Trivy CVE, Checkov misconfiguration, Falco alert, or IAM over-permission you fixed. This becomes a direct "tell me about a vulnerability you found" answer bank.
              <br /><br />
              <code style={{ background: "#111113", padding: "10px 14px", borderRadius: 6, display: "block", fontSize: 12, color: "#fca5a5", lineHeight: 2 }}>
                Finding: <br/>
                Tool: Trivy / Checkov / Falco / IAM{"\n"}
                Severity: <br/>
                Fix: <br/>
                Why it mattered:
              </code>
            </InfoCard>
            <InfoCard title="Where to keep it" icon="🗂️" color="#60a5fa">
              <strong style={{ color: "#fafafa" }}>Private GitHub repo</strong> — markdown files, version controlled, shows employers consistent work over months. Best option.
              <br /><br />
              <strong style={{ color: "#fafafa" }}>Obsidian</strong> — free, local, great for linking notes together.
              <br /><br />
              <a href="https://obsidian.md/" target="_blank" rel="noopener noreferrer" style={{ color: "#60a5fa" }}>Get Obsidian →</a>
            </InfoCard>
            <InfoCard title="Journal becomes portfolio" icon="🏆" color="#a78bfa">
              By Stage 8 your journal IS your portfolio. Clean it up — write a README for every project explaining what it does, why you built it, how to run it. Real findings fixed on real hardware beats a cert with nothing behind it every time.
            </InfoCard>
          </div>
        )}

        {/* GETTING HIRED */}
        {tab === "jobs" && (
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            <InfoCard title="When to start applying" icon="📅" color="#4ade80">
              <strong style={{ color: "#fafafa" }}>Around Stage 5-6</strong> (month 5-6). By then your lab has Linux, Python, AWS, Terraform, Docker, and Kubernetes with security scanning and policy enforcement. That's enough for junior DevSecOps roles.
              <br /><br />
              Don't wait for Stage 8. Apply while finishing the last stages.
            </InfoCard>
            <InfoCard title="Your easiest path in — read this first" icon="🎯" color="#f87171">
              Of the realistic options, <strong style={{ color: "#fafafa" }}>Junior DevSecOps in govtech (DC/NoVA) is likely your strongest fit</strong> — not despite the "Sec," but because of it.
              <br /><br />
              Most junior candidates applying to govtech have zero hands-on security tooling experience. You'll have Trivy, Checkov, Falco, and OPA — hands-on, on hardware you own, with a journal documenting real findings. Combined with US citizenship and DC/NoVA willingness, that's genuinely uncommon at junior level.
              <br /><br />
              Apply broadly — general DevOps as backup, govtech DevSecOps as primary.
            </InfoCard>
            <InfoCard title="Job titles to apply for" icon="🎯" color="#60a5fa">
              • Junior DevSecOps Engineer<br />
              • Junior DevOps Engineer (security emphasis in resume)<br />
              • Associate Cloud Security Engineer<br />
              • Infrastructure Engineer<br />
              • Site Reliability Engineer (Junior)
            </InfoCard>
            <InfoCard title="What makes you stand out as a junior" icon="⭐" color="#facc15">
              Most junior candidates have only courses and certs. You'll have a running Kubernetes cluster with policy enforcement, a CI/CD pipeline with security gates, Trivy/Checkov scan history, Falco alerts, and Python automation tools — all on hardware you own.
              <br /><br />
              In interviews say: <em style={{ color: "#fafafa" }}>"I built a CI/CD pipeline that fails the build on critical vulnerabilities, enforced Pod Security Standards with OPA Gatekeeper on my home Kubernetes cluster, and used Falco to detect a runtime security event I triggered myself. Here's my GitHub."</em>
            </InfoCard>
            <InfoCard title="Certs — do them after building skills" icon="🏅" color="#a78bfa">
              <a href="https://www.comptia.org/certifications/security" target="_blank" rel="noopener noreferrer" style={{ color: "#a78bfa" }}>CompTIA Security+</a> — start during Stage 4, required for most govtech roles<br />
              <a href="https://aws.amazon.com/certification/certified-solutions-architect-associate/" target="_blank" rel="noopener noreferrer" style={{ color: "#a78bfa" }}>AWS Solutions Architect Associate</a> — after Stage 3-4<br />
              <a href="https://developer.hashicorp.com/terraform/tutorials/certification-003" target="_blank" rel="noopener noreferrer" style={{ color: "#a78bfa" }}>Terraform Associate</a> — after Stage 4<br />
              <a href="https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/" target="_blank" rel="noopener noreferrer" style={{ color: "#a78bfa" }}>CKA</a> — after Stage 5<br />
              <a href="https://aws.amazon.com/certification/certified-security-specialty/" target="_blank" rel="noopener noreferrer" style={{ color: "#a78bfa" }}>AWS Security – Specialty</a> — strongest signal for DevSecOps
            </InfoCard>
            <InfoCard title="Where to find jobs" icon="🔍" color="#fb923c">
              <a href="https://linkedin.com/jobs" target="_blank" rel="noopener noreferrer" style={{ color: "#fb923c" }}>LinkedIn</a> — alerts for the titles above<br />
              <a href="https://levels.fyi" target="_blank" rel="noopener noreferrer" style={{ color: "#fb923c" }}>levels.fyi</a> — salary check<br />
              Company career pages directly · Greenhouse, Lever
            </InfoCard>
          </div>
        )}

        {/* GOVTECH */}
        {tab === "govtech" && (
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            <InfoCard title="Your situation" icon="🇺🇸" color="#4ade80">
              US citizen, open to DC/Northern Virginia — a strong starting position. Citizenship is required for most cleared roles, and DC/NoVA is the highest-demand market in the country for this work, especially DevSecOps.
            </InfoCard>
            <InfoCard title="DevSecOps is the highest-leverage title here" icon="💰" color="#f87171">
              Compliance frameworks (FedRAMP, NIST, RMF) require security baked into every pipeline — and most engineers can't do that yet. Your lab build is designed specifically to fill that gap.
            </InfoCard>
            <InfoCard title="Add: Security+ certification" icon="🎯" color="#facc15">
              Required for many entry-level cleared roles under <strong style={{ color: "#fafafa" }}>DoD 8570/8140</strong>.
              <br /><br />
              • Start studying during Stage 4 (4–6 weeks)<br />
              • Exam around the start of Stage 5<br />
              • Runs in parallel, doesn't block the build
              <br /><br />
              <a href="https://www.comptia.org/certifications/security" target="_blank" rel="noopener noreferrer" style={{ color: "#facc15" }}>CompTIA Security+ →</a>
            </InfoCard>
            <InfoCard title="You don't need clearance to apply" icon="🔓" color="#a78bfa">
              Clearance is employer-sponsored, after hiring. Look for <em style={{ color: "#fafafa" }}>"must be able to obtain a security clearance"</em> — often doesn't require one to start. The process (months to over a year) runs in the background once employed.
            </InfoCard>
            <InfoCard title="Companies to target" icon="🏢" color="#fb923c">
              Booz Allen Hamilton · GDIT · Leidos · SAIC · CACI · ManTech · Parsons · Peraton
              <br /><br />
              All regularly hire entry-level DevSecOps/cloud and are concentrated in DC/NoVA.
            </InfoCard>
            <InfoCard title="Where to search" icon="🔍" color="#22d3ee">
              <a href="https://www.clearancejobs.com" target="_blank" rel="noopener noreferrer" style={{ color: "#22d3ee" }}>ClearanceJobs.com</a> — filter "no clearance required"<br />
              <a href="https://www.usajobs.gov" target="_blank" rel="noopener noreferrer" style={{ color: "#22d3ee" }}>USAJobs.gov</a> — direct federal roles<br />
              LinkedIn — alerts for company names + "entry level DevSecOps"
              <br /><br />
              <code style={{ background: "#111113", padding: "8px 12px", borderRadius: 6, display: "block", fontSize: 12, color: "#67e8f9", marginTop: 6, lineHeight: 1.8 }}>
                "DevSecOps engineer" entry level "must be able to obtain"{"\n"}
                "cloud engineer" junior Security+ clearance eligible
              </code>
            </InfoCard>
            <InfoCard title="Timeline summary" icon="📅" color="#4ade80">
              <code style={{ background: "#111113", padding: "10px 14px", borderRadius: 6, display: "block", fontSize: 12, color: "#86efac", lineHeight: 2 }}>
                Stages 1-4   ~4 months{"\n"}
                             + Security+ study (Stage 4){"\n"}
                {"\n"}
                Stage 4-5    Take Security+ exam{"\n"}
                             Start applying{"\n"}
                {"\n"}
                Stages 5-8   ~5 months{"\n"}
                             Interview + clearance process begins{"\n"}
                {"\n"}
                Month 5-12+  Working as Jr DevSecOps Engineer{"\n"}
                             Clearance completes during employment
              </code>
            </InfoCard>
          </div>
        )}

      </div>
    </div>
  );
}

// ─── HELPERS ─────────────────────────────────────────────────────────────────

function SectionLabel({ color, children }) {
  return (
    <div style={{
      fontSize: 11, color, fontWeight: 600,
      letterSpacing: "0.08em", textTransform: "uppercase",
      marginBottom: 8,
    }}>{children}</div>
  );
}

function Section({ color, icon, label, children }) {
  return (
    <div style={{
      marginBottom: 18,
      background: "#111113",
      border: `1px solid ${color}33`,
      borderRadius: 8,
      padding: "12px 14px",
    }}>
      <div style={{
        fontSize: 11, color, fontWeight: 600,
        letterSpacing: "0.08em", textTransform: "uppercase",
        marginBottom: 7,
      }}>{icon ? `${icon} ` : ""}{label}</div>
      <div style={{ fontSize: 13, color: "#a1a1aa", lineHeight: 1.7 }}>{children}</div>
    </div>
  );
}

function InfoCard({ title, icon, color, children }) {
  return (
    <div style={{
      background: "#111113",
      border: "1px solid #27272a",
      borderRadius: 10,
      padding: "18px 20px",
    }}>
      <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 }}>
        <span style={{ fontSize: 18 }}>{icon}</span>
        <span style={{ fontWeight: 600, fontSize: 15, color: "#fafafa" }}>{title}</span>
      </div>
      <div style={{ fontSize: 13, color: "#71717a", lineHeight: 1.8 }}>{children}</div>
    </div>
  );
}
