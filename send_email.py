import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_test_email():
    # 1. 读取配置（从环境变量获取，避免硬编码）
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    sender = os.getenv("EMAIL_USERNAME")
    sender_pwd = os.getenv("EMAIL_PASSWORD")
    receivers = os.getenv("EMAIL_RECEIVER").split(",")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    run_status = os.getenv("JOB_STATUS")
    run_url = os.getenv("GITHUB_RUN_URL")

    # 2. 构建邮件内容
    msg = MIMEMultipart()
    msg["From"] = f"GitHub Actions <{sender}>"
    msg["To"] = ",".join(receivers)
    msg["Subject"] = f"【Behave测试报告】{repo_name} - {run_status}"

    # 邮件正文（HTML格式，可自定义样式）
    body = f"""
    <h2>Behave测试执行结果</h2>
    <p>测试分支：{os.getenv("GITHUB_REF_NAME")}</p>
    <p>提交信息：{os.getenv("GITHUB_HEAD_COMMIT_MESSAGE")}</p>
    <p>测试状态：<span style="color: {'red' if run_status == 'failure' else 'green'}">{run_status}</span></p>
    <p>运行时长：{os.getenv("JOB_DURATION")}</p>
    <p>查看详情：<a href="{run_url}">{run_url}</a></p>
    <p>测试报告附件见下方，请下载查看。</p>
    """
    msg.attach(MIMEText(body, "html", "utf-8"))

    # 附件：测试报告（test-report.html）
    report_path="reports/test-report.html"
    if os.path.exists(report_path):
        with open(report_path, "rb") as f:
            att = MIMEApplication(f.read())
            att.add_header("Content-Disposition", "attachment", filename=report_path)
            msg.attach(att)

    # 3. 发送邮件
    try:
        # 连接SMTP服务器（以SSL为例）
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender, sender_pwd)
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()
        print("测试邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败：{str(e)}")
        raise

if __name__ == "__main__":
    send_test_email()