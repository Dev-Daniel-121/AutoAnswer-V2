from project import LogType

class CollectTaskInfos:
    def __init__(self, page, 
                component_class,
                title_activity_class,
                user_activity_class,
                author_activity_class,
                class_activity_class,
                expire_activity_class,
                id_activity_class
            ):
        self.page = page
        self.component_class = component_class
        self.title_activity_class = title_activity_class
        self.user_activity_class = user_activity_class
        self.author_activity_class = author_activity_class
        self.class_activity_class = class_activity_class
        self.expire_activity_class = expire_activity_class
        self.id_activity_class = id_activity_class

    def extract_clean_text(self, selector):
        return self.page.locator(selector).evaluate(
            '''
            node => {
                const label = node.querySelector(\'p\');
                return node.textContent.replace(label?.textContent || \'\', \'\').trim();
            }
            '''
        )
    
    def component(self):
        try:
            component = self.page.locator(self.component_class).inner_text()
            return component
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informação: {e}')
            return

    def title_activity(self):
        try:
            title_activity = self.page.locator(self.title_activity_class).inner_text()
            return title_activity
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informação: {e}')
            return

    def user_activity(self):
        try:
            user_activity = self.extract_clean_text(self.user_activity_class)
            return user_activity
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informação: {e}')
            return

    def author_activity(self):
        try:
            author_activity = self.extract_clean_text(self.author_activity_class)
            return author_activity
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informação: {e}')
            return

    def class_activity(self):
        try:
            class_activity = self.extract_clean_text(self.class_activity_class)
            return class_activity
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informação: {e}')
            return

    def expire_activity(self):
        try:
            expire_activity = self.extract_clean_text(self.expire_activity_class)
            return expire_activity
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informação: {e}')
            return

    def id_activity(self):
        try:
            id_activity = self.extract_clean_text(self.id_activity_class)
            return id_activity
        except Exception as e:
            print(f'[{LogType.ERROR}] Erro ao obter informação: {e}')
            return

    def run(self):
        print(f'[{LogType.INFO}] Coletando informações da Atividade...\n')
        
        component = self.component()
        title_activity = self.title_activity()
        user_activity = self.user_activity()
        author_activity = self.author_activity()
        class_activity = self.class_activity()
        expire_activity = self.expire_activity()
        id_activity = self.id_activity()

        return component, title_activity, user_activity, author_activity, class_activity, expire_activity, id_activity