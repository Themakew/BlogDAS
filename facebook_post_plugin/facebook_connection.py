import facebook


def main(message, page_id, access_token):
    # Customize the page_id and the access_token to your facebook page
    cfg = {
        "page_id": page_id,
        "access_token": access_token
    }

    api = get_api(cfg)
    msg = message
    api.put_wall_post(msg)


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    return graph
