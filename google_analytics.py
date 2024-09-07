import streamlit as st
import streamlit.components.v1 as components

def add_google_analytics(tracking_id):
    components.html(
        f"""
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={tracking_id}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{tracking_id}');
        </script>
        """,
        height=0,
        width=0,
    )