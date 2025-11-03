FROM ghcr.io/home-assistant/home-assistant:stable

COPY --link ./config-templates /dummy-user/config-templates
COPY --link ./entrypoint.sh ./replace_secrets.py /dummy-user/

ENTRYPOINT [ "/dummy-user/entrypoint.sh" ]