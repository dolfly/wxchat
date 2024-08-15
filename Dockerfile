FROM fedora:39
LABEL DESCRIBE="WxChat: Fedora for WeChat, Base on LXDE, Wine, xRDP, WeChatFerry."
RUN dnf update -y \
    && dnf groupinstall -y "LXDE" \
    && dnf install -y wine \
    && dnf install -y xrdp \
    && dnf clean all
WORKDIR /root
COPY data .data
RUN echo "root:wxchat" | chpasswd \ 
    && mkdir ~/Desktop \
    && ln -s /root/.data/*.desktop ~/Desktop/ \
    && unzip -d /root/.data/wcf /root/.data/v39.2.1.zip  \
    && echo "OK"
EXPOSE 3389
EXPOSE 8001
ENTRYPOINT ["/root/.data/bin/entrypoint"]
CMD ["bash"]
