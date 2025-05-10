def collect_media_if_exists(page, card, video_media_selector, img_media_selector):
    try:
        if (
            card.locator(video_media_selector).count() == 0 and
            card.locator(img_media_selector).count() == 0
        ):
            return {'video': {}, 'image': {}, 'gif': {}}

        from project.apps.sala_do_futuro.models.realizar_atividades.models.collect_info import CollectMedia
        media_collector = CollectMedia(
            page=page,
            card=card,
            video_media_selector=video_media_selector,
            img_media_selector=img_media_selector
        )
        return media_collector.extract_media()
    except Exception as e:
        print(f'[MediaUtils] Erro ao coletar mídia condicionalmente: {e}')
        return {'video': {}, 'image': {}, 'gif': {}}
