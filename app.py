import streamlit as st
import chatter

chat = chatter.Chatter()
with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Get current tab from query params
query_params = st.experimental_get_query_params()
current_tab = query_params.get("tab", ["tab_default"])[0]

if current_tab == "tab_default":
    st.title("以下のテーマでメルマガを書いてください。")

    subject = st.text_input(label="テーマ", value="", placeholder="制: 自己啓発")
    tokens = st.text_input(label="制限文字数", value="", placeholder="制: 800字")
    sender_ages = st.text_input(label="送りての属性", value="", placeholder="制: 30代女性")
    recipient_ages = st.text_input(label="受けての属性", value="", placeholder="制: 40代男性")
    trends = st.text_input(label="文体のテイスト", value="", placeholder="制: テンション高め")
    no_variable = st.text_input(label="元ネタはりつけ", value="", placeholder="制: ")
    languages = st.text_input(label="言語", value="", placeholder="制: 日本語")
    template_results = st.text_input(label="文例数", value="", placeholder="制: 1,2,3")

    generate_email = st.button("作成", key="button_abc")

    if generate_email:
        job = {
            "subject": subject,
            "tokens": tokens,
            "sender_ages": sender_ages,
            "recipient_ages": recipient_ages,
            "trends": trends,
            "no_variable": no_variable,
            "languages": languages,
            "template_results": template_results
        }

        # Save data to session
        st.session_state.job = job

        # Set query params and reload page
        st.experimental_set_query_params(tab="tab_step")
        st.experimental_rerun()

else:
    # Get data in session
    job = st.session_state.job

    if job:
        messages = chat.email_from_job(job=job)
        for index, message in enumerate(messages):
            if index == 0:
                st.write("オプション 1:")
                st.code(message, language="python")
            elif index == 1:
                st.write("オプション 2:")
                st.code(message, language="python")
            else:
                st.write("オプション 3:")
                st.code(message, language="python")

    tab_back = st.button("戻る")
    if tab_back:
        st.experimental_set_query_params(tab="tab_default")
        st.experimental_rerun()
