import json

prototype_data = {
    "brand_name": "Terra Vivo",
    "sidebar": [
        {
            "id": "menu-conteudos",
            "title": "Conteúdos",
            "icon": "fas fa-file-alt",
            "items": [
                {"id": "home", "title": "Lista de Serviços", "view": "home"}
            ]
        },
        {
            "id": "menu-categorias",
            "title": "Organização",
            "icon": "fas fa-tags",
            "items": [
                {"id": "categorias-loja", "title": "Árvore de Categorias", "view": "categorias-loja"}
            ]
        },
        {
            "id": "menu-publicidade",
            "title": "Publicidade",
            "icon": "fas fa-bullhorn",
            "items": [
                {"id": "banners-lista", "title": "Lista de Banners", "view": "banners-lista"},
                {"id": "carrossel", "title": "Carrossel de Banners", "view": "carrossel"}
            ]
        }
    ]
}

views = {}

views["login"] = """
    <div class="min-h-screen flex items-center justify-center bg-gray-900 bg-opacity-50" style="background-image: url('https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=2000&q=80'); background-size: cover; background-position: center;">
        <div class="absolute inset-0 bg-indigo-900 opacity-80 mix-blend-multiply"></div>
        <div class="relative w-full max-w-md bg-white rounded-2xl shadow-2xl overflow-hidden z-10">
            <div class="bg-indigo-600 p-6 text-center">
                <h1 class="text-3xl font-bold text-white tracking-wider">TERRA <span class="font-light">VIVO</span></h1>
                <p class="text-indigo-200 text-sm mt-2">Painel de Gerenciamento</p>
            </div>
            <div class="p-8">
                <form @submit.prevent="currentView = 'home'">
                    <div class="mb-5">
                        <label class="block text-sm font-medium text-gray-700 mb-2">ID do Usuário</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <i class="fas fa-user text-gray-400"></i>
                            </div>
                            <input type="text" class="w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-gray-50 text-gray-900" placeholder="81021595" value="81021595">
                        </div>
                    </div>
                    <div class="mb-5">
                        <label class="block text-sm font-medium text-gray-700 mb-2">Senha</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <i class="fas fa-lock text-gray-400"></i>
                            </div>
                            <input type="password" class="w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-gray-50 text-gray-900" placeholder="••••••••" value="password">
                        </div>
                    </div>
                    <div class="flex items-center mb-6">
                        <input type="checkbox" id="userTerra" class="w-4 h-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500" checked>
                        <label for="userTerra" class="ml-2 text-sm text-gray-600">Usuário Rede Terra</label>
                    </div>
                    <button type="submit" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-4 rounded-lg shadow transition-colors flex justify-center items-center gap-2">
                        <span>Acessar Painel</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </form>
            </div>
        </div>
    </div>
"""

views["home"] = """
    <div class="mb-6 flex justify-between items-center">
        <h2 class="text-2xl font-bold text-gray-800">Serviços <span class="text-gray-400 font-normal">| Conteúdos</span></h2>
        <button @click="currentView = 'novo-pno'" class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg shadow shadow-indigo-200 font-medium flex items-center gap-2 transition-colors">
            <i class="fas fa-plus"></i> Adicionar Serviço
        </button>
    </div>
    <div class="bg-white p-5 rounded-xl shadow-sm border border-gray-100 mb-6">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div><label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Código PNO</label><input type="text" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"></div>
            <div><label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Nome do Serviço</label><input type="text" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"></div>
            <div>
                <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Fornecedor</label>
                <select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>Todos os fornecedores</option></select>
            </div>
            <div class="flex items-end">
                <button class="w-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium py-2 px-4 rounded-lg transition-colors flex justify-center items-center gap-2"><i class="fas fa-search"></i> Filtrar Resultados</button>
            </div>
        </div>
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="px-6 py-4 border-b border-gray-100 flex justify-between items-center bg-gray-50">
            <span class="text-sm text-gray-500 font-medium">Mostrando 1 de 1 registros</span>
        </div>
        <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-white">
                    <tr>
                        <th class="px-6 py-4 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">PNO</th>
                        <th class="px-6 py-4 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Serviço</th>
                        <th class="px-6 py-4 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Fornecedor</th>
                        <th class="px-6 py-4 text-center text-xs font-bold text-gray-500 uppercase tracking-wider">Status</th>
                        <th class="px-6 py-4 text-right text-xs font-bold text-gray-500 uppercase tracking-wider">Ações</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                    <tr class="hover:bg-gray-50">
                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-indigo-600">63650</td>
                        <td class="px-6 py-4 text-sm text-gray-900 font-medium">Teatrix Premium</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Digital Virgo</td>
                        <td class="px-6 py-4 whitespace-nowrap text-center"><span class="px-3 py-1 inline-flex text-xs font-semibold rounded-full bg-green-100 text-green-700">Ativo</span></td>
                        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                            <button @click="currentView = 'edicao-pno'" class="text-gray-400 hover:text-indigo-600 transition-colors p-2" title="Editar / Gerenciar"><i class="fas fa-cog text-lg"></i></button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
"""

views["novo-pno"] = """
    <div class="mb-6 flex justify-between items-center">
        <div class="flex items-center gap-3">
            <button @click="currentView = 'home'" class="w-10 h-10 rounded-full bg-white border border-gray-200 flex items-center justify-center text-gray-500 hover:text-indigo-600 hover:border-indigo-200 transition-colors shadow-sm"><i class="fas fa-arrow-left"></i></button>
            <h2 class="text-2xl font-bold text-gray-800">Criar Novo Serviço <span class="text-gray-400 font-normal">| PNO</span></h2>
        </div>
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="px-8 py-6 border-b border-gray-100 bg-gray-50"><h3 class="text-lg font-semibold text-gray-700">Informações Iniciais</h3></div>
        <div class="p-8">
            <form class="space-y-6" @submit.prevent="currentView = 'edicao-pno'">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div><label class="block text-sm font-semibold text-gray-700 mb-2">Código PNO</label><input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2.5 bg-gray-100 text-gray-500 cursor-not-allowed" value="Gerado após salvar" disabled></div>
                    <div><label class="block text-sm font-semibold text-gray-700 mb-2">Nome do Serviço *</label><input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none" required></div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div><label class="block text-sm font-semibold text-gray-700 mb-2">Fornecedor *</label><select class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none" required><option>Digital Virgo</option></select></div>
                    <div><label class="block text-sm font-semibold text-gray-700 mb-2">Classificação</label><select class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none"><option>Entretenimento</option></select></div>
                </div>
                <div class="pt-6 flex justify-end gap-4 border-t border-gray-100">
                    <button type="button" @click="currentView = 'home'" class="px-6 py-2.5 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-colors">Cancelar</button>
                    <button type="submit" class="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 shadow-md transition-colors flex items-center gap-2"><i class="fas fa-save"></i> Criar Serviço</button>
                </div>
            </form>
        </div>
    </div>
"""

views["edicao-pno"] = """
    <div x-data="{ tab: 'dados' }">
        <div class="mb-6 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <button @click="currentView = 'home'" class="w-10 h-10 rounded-full bg-white border border-gray-200 flex items-center justify-center text-gray-500 hover:text-indigo-600 shadow-sm"><i class="fas fa-arrow-left"></i></button>
                <div>
                    <h2 class="text-2xl font-bold text-gray-800">Gerenciar Serviço <span class="text-gray-400 font-normal">| Teatrix Premium</span></h2>
                    <p class="text-sm text-gray-500 mt-1">PNO: 63650</p>
                </div>
            </div>
            <span class="px-3 py-1 bg-green-100 text-green-700 text-sm font-bold rounded-full uppercase tracking-wider">Ativo</span>
        </div>
        
        <div class="flex space-x-1 bg-white p-1 rounded-t-xl border border-gray-200 border-b-0 overflow-x-auto">
            <button @click="tab = 'dados'" :class="tab === 'dados' ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'text-gray-500 hover:bg-gray-50'" class="px-4 py-2.5 text-sm font-medium rounded-lg border border-transparent transition-colors whitespace-nowrap"><i class="fas fa-info-circle mr-2"></i>Dados Básicos</button>
            <button @click="tab = 'descricao'" :class="tab === 'descricao' ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'text-gray-500 hover:bg-gray-50'" class="px-4 py-2.5 text-sm font-medium rounded-lg border border-transparent transition-colors whitespace-nowrap"><i class="fas fa-align-left mr-2"></i>Desc. Comercial</button>
            <button @click="tab = 'categorias'" :class="tab === 'categorias' ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'text-gray-500 hover:bg-gray-50'" class="px-4 py-2.5 text-sm font-medium rounded-lg border border-transparent transition-colors whitespace-nowrap"><i class="fas fa-sitemap mr-2"></i>Categorias</button>
            <button @click="tab = 'multimidia'" :class="tab === 'multimidia' ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'text-gray-500 hover:bg-gray-50'" class="px-4 py-2.5 text-sm font-medium rounded-lg border border-transparent transition-colors whitespace-nowrap"><i class="fas fa-image mr-2"></i>Multimídia</button>
            <button @click="tab = 'ofertas'" :class="tab === 'ofertas' ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'text-gray-500 hover:bg-gray-50'" class="px-4 py-2.5 text-sm font-medium rounded-lg border border-transparent transition-colors whitespace-nowrap"><i class="fas fa-tags mr-2"></i>Ofertas</button>
            <button @click="tab = 'documentacao'" :class="tab === 'documentacao' ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'text-gray-500 hover:bg-gray-50'" class="px-4 py-2.5 text-sm font-medium rounded-lg border border-transparent transition-colors whitespace-nowrap"><i class="fas fa-file-pdf mr-2"></i>Documentação</button>
        </div>
        
        <div class="bg-white rounded-b-xl rounded-tr-xl shadow-sm border border-gray-200 overflow-hidden">
            
            <!-- Dados Básicos -->
            <div x-show="tab === 'dados'" class="p-8">
                <form class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div><label class="block text-sm font-semibold text-gray-700 mb-2">Código PNO</label><input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2.5 bg-gray-100 text-gray-500 cursor-not-allowed" value="63650" disabled></div>
                        <div><label class="block text-sm font-semibold text-gray-700 mb-2">Nome do Serviço</label><input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none" value="Teatrix Premium"></div>
                    </div>
                    <div class="pt-6 flex justify-end gap-4 border-t border-gray-100">
                        <button type="button" class="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-colors flex items-center gap-2"><i class="fas fa-check"></i> Salvar Dados</button>
                    </div>
                </form>
            </div>

            <!-- Descrição Comercial -->
            <div x-show="tab === 'descricao'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Informações para Exibição Comercial</h3>
                <form class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div><label class="block text-sm font-semibold text-gray-700 mb-2">Idioma</label><select class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none"><option>Português (Brasil)</option></select></div>
                        <div><label class="block text-sm font-semibold text-gray-700 mb-2">Nome Comercial</label><input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none" value="Teatrix Premium BR"></div>
                    </div>
                    <div class="pt-6 flex justify-end border-t border-gray-100">
                        <button type="button" class="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 flex items-center gap-2"><i class="fas fa-check"></i> Salvar Descrição</button>
                    </div>
                </form>
            </div>

            <!-- Categorias Tab (New) -->
            <div x-show="tab === 'categorias'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Categorização do PNO</h3>
                <div class="flex gap-6">
                    <!-- Tree View -->
                    <div class="w-1/3 bg-gray-50 border border-gray-200 rounded-lg p-4 h-80 overflow-y-auto">
                        <ul class="space-y-2 text-sm text-gray-700">
                            <li>
                                <div class="flex items-center gap-2 cursor-pointer"><i class="fas fa-caret-down text-gray-400"></i><i class="fas fa-folder-open text-indigo-400"></i> ROOT</div>
                                <ul class="ml-5 mt-2 space-y-2 border-l border-gray-200 pl-3">
                                    <li class="flex items-center gap-2"><input type="checkbox" class="rounded text-indigo-600"><i class="fas fa-folder text-yellow-400"></i> Jogos</li>
                                    <li class="flex items-center gap-2"><input type="checkbox" class="rounded text-indigo-600"><i class="fas fa-folder text-yellow-400"></i> Wallpapers</li>
                                    <li class="flex items-center gap-2"><input type="checkbox" checked class="rounded text-indigo-600"><i class="fas fa-folder text-yellow-400"></i> Vídeos</li>
                                    <li class="flex items-center gap-2"><input type="checkbox" class="rounded text-indigo-600"><i class="fas fa-folder text-yellow-400"></i> Promoções</li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                    <!-- Right panel is empty as per prototype, but let's add a save button -->
                    <div class="w-2/3 flex flex-col justify-end">
                        <div class="bg-indigo-50 p-6 rounded-lg border border-indigo-100 mb-auto">
                            <p class="text-indigo-800 text-sm"><i class="fas fa-info-circle mr-2"></i> Selecione à esquerda as categorias onde este serviço deve aparecer nas lojas.</p>
                        </div>
                        <div class="flex justify-end pt-6">
                            <button type="button" class="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 flex items-center gap-2"><i class="fas fa-check"></i> Salvar Categorias</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Multimídia Tab -->
            <div x-show="tab === 'multimidia'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Gerenciamento de Arquivos Multimídia</h3>
                <div class="bg-gray-50 p-6 rounded-xl border border-gray-200 mb-8">
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                        <div><label class="block text-xs font-semibold text-gray-500 uppercase">Idioma</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>PT</option></select></div>
                        <div><label class="block text-xs font-semibold text-gray-500 uppercase">Tipo</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>BANNER</option></select></div>
                        <div><label class="block text-xs font-semibold text-gray-500 uppercase">Arquivo</label><input type="file" class="w-full border border-gray-300 rounded-lg px-3 py-1.5 bg-white"></div>
                    </div>
                    <div class="flex justify-end"><button class="px-6 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700"><i class="fas fa-upload mr-2"></i> Fazer Upload</button></div>
                </div>
                <table class="min-w-full divide-y divide-gray-200 border border-gray-200 rounded-lg">
                    <thead class="bg-gray-50"><tr><th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase">Tipo</th><th class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase">Idioma</th><th class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase">Preview</th></tr></thead>
                    <tbody class="bg-white"><tr class="hover:bg-gray-50"><td class="px-6 py-4 text-sm font-medium">BANNER</td><td class="px-6 py-4 text-sm text-center">PT</td><td class="px-6 py-4 text-center"><i class="fas fa-image text-indigo-500"></i></td></tr></tbody>
                </table>
            </div>

            <!-- Ofertas Tab -->
            <div x-show="tab === 'ofertas'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Ofertas</h3>
                <div class="bg-gray-50 p-6 rounded-xl border border-gray-200 mb-8 grid grid-cols-2 gap-4">
                    <div><label class="block text-xs font-semibold text-gray-500 mb-1">Nome da Oferta</label><input type="text" class="w-full border border-gray-300 rounded-lg px-3 py-2"></div>
                    <div><label class="block text-xs font-semibold text-gray-500 mb-1">Preço Final</label><input type="number" class="w-full border border-gray-300 rounded-lg px-3 py-2" value="32.90"></div>
                    <div class="col-span-2 flex justify-end"><button class="px-6 py-2 bg-indigo-600 text-white font-medium rounded-lg"><i class="fas fa-plus mr-2"></i> Adicionar Oferta</button></div>
                </div>
                <table class="min-w-full divide-y divide-gray-200 border border-gray-200 rounded-lg">
                    <thead class="bg-gray-50"><tr><th class="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase">Nome</th><th class="px-4 py-3 text-center text-xs font-bold text-gray-500 uppercase">Valor Final</th><th class="px-4 py-3 text-center text-xs font-bold text-gray-500 uppercase">Segmento</th></tr></thead>
                    <tbody class="bg-white"><tr class="hover:bg-gray-50"><td class="px-4 py-4 text-sm font-medium">Vale Saúde Farma</td><td class="px-4 py-4 text-sm font-bold text-indigo-600 text-center">R$ 32,90</td><td class="px-4 py-4 text-xs text-gray-500 text-center">POS | CONTROLE</td></tr></tbody>
                </table>
            </div>

            <!-- Documentação Tab -->
            <div x-show="tab === 'documentacao'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Manuais e T&C</h3>
                <div class="bg-gray-50 p-5 rounded-xl border border-gray-200 mb-4 flex items-end gap-4">
                    <div class="w-1/3"><label class="block text-xs font-semibold text-gray-500 uppercase">Idioma</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2"><option>PT</option></select></div>
                    <div class="w-1/2"><label class="block text-xs font-semibold text-gray-500 uppercase">Arquivo PDF</label><input type="file" class="w-full border border-gray-300 rounded-lg px-3 py-1.5 bg-white"></div>
                    <button class="px-6 py-2 bg-indigo-600 text-white rounded-lg"><i class="fas fa-upload mr-2"></i> Enviar</button>
                </div>
                <table class="min-w-full divide-y divide-gray-200 border border-gray-200 rounded-lg">
                    <thead class="bg-gray-100"><tr><th class="px-4 py-2 text-left text-xs font-bold text-gray-500">Idioma</th><th class="px-4 py-2 text-left text-xs font-bold text-gray-500">Arquivo</th></tr></thead>
                    <tbody class="bg-white"><tr><td class="px-4 py-3 text-sm font-medium">PT</td><td class="px-4 py-3 text-sm text-indigo-600"><i class="fas fa-file-pdf mr-2 text-red-500"></i> manual.pdf</td></tr></tbody>
                </table>
            </div>
        </div>
    </div>
"""

views["categorias-loja"] = """
    <div class="mb-6 flex justify-between items-center">
        <h2 class="text-2xl font-bold text-gray-800">Organização <span class="text-gray-400 font-normal">| Árvore de Categorias</span></h2>
    </div>
    
    <div class="flex gap-6 h-[calc(100vh-200px)]">
        <!-- Tree View -->
        <div class="w-1/3 bg-white border border-gray-200 rounded-xl shadow-sm p-4 overflow-y-auto">
            <h3 class="text-sm font-bold text-gray-500 uppercase tracking-wider mb-4 px-2">Estrutura das Lojas</h3>
            <ul class="space-y-2 text-sm text-gray-700">
                <li>
                    <div class="flex items-center gap-2 cursor-pointer py-1 px-2 hover:bg-gray-50 rounded"><i class="fas fa-caret-down text-gray-400"></i><i class="fas fa-shopping-bag text-indigo-500"></i> Vivo Store BR</div>
                    <ul class="ml-5 mt-1 space-y-1 border-l border-gray-200 pl-3">
                        <li class="flex items-center gap-2 py-1 px-2 hover:bg-gray-50 rounded cursor-pointer"><i class="fas fa-folder text-yellow-400"></i> Entretenimento</li>
                        <li class="flex items-center gap-2 py-1 px-2 hover:bg-gray-50 rounded cursor-pointer bg-indigo-50 text-indigo-700 font-medium"><i class="fas fa-folder-open text-yellow-500"></i> Educação</li>
                        <li class="flex items-center gap-2 py-1 px-2 hover:bg-gray-50 rounded cursor-pointer"><i class="fas fa-folder text-yellow-400"></i> Saúde & Bem-estar</li>
                        <li class="flex items-center gap-2 py-1 px-2 hover:bg-gray-50 rounded cursor-pointer"><i class="fas fa-folder text-yellow-400"></i> Segurança</li>
                    </ul>
                </li>
            </ul>
        </div>
        
        <!-- Editor -->
        <div class="w-2/3 bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden flex flex-col">
            <div class="px-8 py-6 border-b border-gray-100 bg-gray-50">
                <h3 class="text-lg font-semibold text-gray-700">Editar Categoria Selecionada</h3>
            </div>
            <div class="p-8 flex-1">
                <form class="space-y-6">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Nome da Categoria</label>
                        <input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none focus:ring-2 focus:ring-indigo-500" value="Educação">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Lista Priorizada</label>
                        <select class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none focus:ring-2 focus:ring-indigo-500"><option>Nenhuma</option></select>
                    </div>
                    
                    <div class="pt-4 flex gap-6">
                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="w-5 h-5 text-indigo-600 rounded"><span class="text-sm font-medium text-gray-700">Categoria Principal</span></label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="w-5 h-5 text-indigo-600 rounded"><span class="text-sm font-medium text-gray-700">Contéudo Adulto</span></label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="w-5 h-5 text-indigo-600 rounded" checked><span class="text-sm font-medium text-gray-700">Recomendada</span></label>
                    </div>
                    
                    <div class="pt-8 flex justify-end gap-4 border-t border-gray-100 mt-auto">
                        <button type="button" class="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 shadow-md transition-colors flex items-center gap-2"><i class="fas fa-save"></i> Salvar Alterações</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
"""

views["banners-lista"] = """
    <div class="mb-6 flex justify-between items-center">
        <h2 class="text-2xl font-bold text-gray-800">Publicidade <span class="text-gray-400 font-normal">| Gerenciar Banners</span></h2>
        <button @click="currentView = 'banner-novo'" class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg shadow shadow-indigo-200 font-medium flex items-center gap-2 transition-colors">
            <i class="fas fa-image"></i> Novo Banner
        </button>
    </div>
    
    <div class="bg-white p-5 rounded-xl shadow-sm border border-gray-100 mb-6">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div><label class="block text-xs font-semibold text-gray-500 uppercase mb-1">Loja</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>BR VIVO STORE</option></select></div>
            <div><label class="block text-xs font-semibold text-gray-500 uppercase mb-1">Operadora</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>VIVO BRASIL</option></select></div>
            <div class="flex items-end"><button class="w-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium py-2 px-4 rounded-lg"><i class="fas fa-filter"></i> Filtrar</button></div>
        </div>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
                <tr>
                    <th class="px-6 py-4 text-left text-xs font-bold text-gray-500 uppercase">ID</th>
                    <th class="px-6 py-4 text-left text-xs font-bold text-gray-500 uppercase">Preview</th>
                    <th class="px-6 py-4 text-left text-xs font-bold text-gray-500 uppercase">Campanha</th>
                    <th class="px-6 py-4 text-center text-xs font-bold text-gray-500 uppercase">Status</th>
                    <th class="px-6 py-4 text-right text-xs font-bold text-gray-500 uppercase">Ações</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 bg-white">
                <tr class="hover:bg-gray-50">
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">1653</td>
                    <td class="px-6 py-4 whitespace-nowrap"><div class="w-16 h-8 bg-red-500 rounded flex items-center justify-center text-white text-xs font-bold shadow-inner">NETFLIX</div></td>
                    <td class="px-6 py-4 text-sm text-gray-700 font-medium">NETFLIX_01_09_2026</td>
                    <td class="px-6 py-4 whitespace-nowrap text-center"><span class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-700">Ativo</span></td>
                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"><button @click="currentView = 'banner-novo'" class="text-gray-400 hover:text-indigo-600 p-2"><i class="fas fa-edit"></i></button></td>
                </tr>
            </tbody>
        </table>
    </div>
"""

views["banner-novo"] = """
    <div class="mb-6 flex justify-between items-center">
        <div class="flex items-center gap-3">
            <button @click="currentView = 'banners-lista'" class="w-10 h-10 rounded-full bg-white border border-gray-200 flex items-center justify-center text-gray-500 hover:text-indigo-600 shadow-sm"><i class="fas fa-arrow-left"></i></button>
            <h2 class="text-2xl font-bold text-gray-800">Criar Novo Banner</h2>
        </div>
    </div>
    
    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="px-8 py-6 border-b border-gray-100 bg-gray-50 flex gap-6">
            <p class="text-sm"><span class="font-bold text-gray-700">Loja:</span> BR VIVO STORE</p>
            <p class="text-sm"><span class="font-bold text-gray-700">Operadora:</span> VIVO BRASIL</p>
        </div>
        
        <div class="p-8">
            <form class="space-y-6" @submit.prevent="currentView = 'banners-lista'">
                <div class="flex flex-wrap items-center gap-6 mb-4">
                    <div class="flex-1 min-w-[300px]">
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Nome da Campanha</label>
                        <input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2.5 outline-none focus:ring-2 focus:ring-indigo-500" required>
                    </div>
                    <div class="flex items-center gap-4 mt-6">
                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="w-5 h-5 text-indigo-600 rounded" checked><span class="text-sm font-medium text-gray-700">Ativo</span></label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="w-5 h-5 text-indigo-600 rounded"><span class="text-sm font-medium text-gray-700">Contéudo Adulto</span></label>
                    </div>
                </div>

                <div class="border-t border-gray-100 pt-6 pb-2">
                    <label class="block text-sm font-semibold text-gray-700 mb-4">Tipo de Banner</label>
                    <div class="flex gap-6">
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="tipo_banner" class="w-4 h-4 text-indigo-600" checked><span class="text-sm font-medium text-gray-700">URL Referenciada</span></label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="tipo_banner" class="w-4 h-4 text-indigo-600"><span class="text-sm font-medium text-gray-700">Conteúdo (PNO)</span></label>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 bg-gray-50 p-6 rounded-lg border border-gray-200">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2"><i class="fas fa-mobile-alt mr-2"></i>Imagem para Mobile</label>
                        <input type="file" class="w-full border border-gray-300 rounded-lg px-3 py-2 bg-white">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2"><i class="fas fa-desktop mr-2"></i>Imagem para Desktop</label>
                        <input type="file" class="w-full border border-gray-300 rounded-lg px-3 py-2 bg-white">
                    </div>
                </div>

                <div class="pt-6 flex justify-end gap-4 border-t border-gray-100">
                    <button type="button" @click="currentView = 'banners-lista'" class="px-6 py-2.5 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50">Cancelar</button>
                    <button type="submit" class="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 shadow-md flex items-center gap-2"><i class="fas fa-save"></i> Salvar Banner</button>
                </div>
            </form>
        </div>
    </div>
"""

views["carrossel"] = """
    <div class="mb-6 flex justify-between items-center">
        <h2 class="text-2xl font-bold text-gray-800">Publicidade <span class="text-gray-400 font-normal">| Carrossel de Destaques</span></h2>
    </div>
    
    <!-- Filtro Superior (Step 1) -->
    <div class="bg-indigo-900 p-5 rounded-t-xl shadow-sm flex flex-wrap gap-4 items-end">
        <div class="w-64">
            <label class="block text-xs font-semibold text-indigo-200 uppercase mb-1">Loja</label>
            <select class="w-full border-none rounded-lg px-3 py-2 bg-white/10 text-white outline-none focus:ring-2 focus:ring-indigo-400"><option>BR VIVO STORE</option></select>
        </div>
        <div class="w-64">
            <label class="block text-xs font-semibold text-indigo-200 uppercase mb-1">Operadora</label>
            <select class="w-full border-none rounded-lg px-3 py-2 bg-white/10 text-white outline-none focus:ring-2 focus:ring-indigo-400"><option>VIVO BRASIL</option></select>
        </div>
        <div class="w-64">
            <label class="block text-xs font-semibold text-indigo-200 uppercase mb-1">Carrossel (Posição)</label>
            <select class="w-full border-none rounded-lg px-3 py-2 bg-white/10 text-white outline-none focus:ring-2 focus:ring-indigo-400"><option>Prime Zone</option></select>
        </div>
        <button class="bg-indigo-500 hover:bg-indigo-400 text-white font-medium py-2 px-6 rounded-lg shadow"><i class="fas fa-sync-alt mr-2"></i> Carregar</button>
    </div>

    <!-- Layout Dividido (Step 2) -->
    <div class="flex bg-white rounded-b-xl border border-t-0 border-gray-200 shadow-sm min-h-[500px]">
        
        <!-- Banners Ativos no Carrossel (Esquerda) -->
        <div class="w-2/3 border-r border-gray-200 p-6">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-sm font-bold text-gray-700 uppercase">Itens no Carrossel (Arrastar para ordenar)</h3>
                <button class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white text-sm font-medium rounded-lg shadow-sm"><i class="fas fa-save mr-2"></i> Salvar Ordem</button>
            </div>
            
            <div class="space-y-3">
                <!-- Item 1 -->
                <div class="flex items-center bg-gray-50 border border-gray-200 rounded-lg p-3 cursor-move hover:bg-indigo-50 hover:border-indigo-200 transition-colors">
                    <div class="text-gray-400 px-3"><i class="fas fa-grip-vertical"></i></div>
                    <div class="w-24 h-12 bg-gray-800 rounded flex items-center justify-center text-white text-[10px] font-bold overflow-hidden shadow-inner mr-4">
                        <img src="https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80" class="w-full h-full object-cover opacity-70">
                    </div>
                    <div class="flex-1">
                        <p class="text-xs text-gray-500">Banner #1641</p>
                        <p class="text-sm font-bold text-gray-800">GEMINI_AI_17_06_2026</p>
                    </div>
                    <button class="w-8 h-8 rounded-full text-red-500 hover:bg-red-50 flex items-center justify-center transition-colors"><i class="fas fa-times"></i></button>
                </div>
                
                <!-- Item 2 -->
                <div class="flex items-center bg-gray-50 border border-gray-200 rounded-lg p-3 cursor-move hover:bg-indigo-50 hover:border-indigo-200 transition-colors">
                    <div class="text-gray-400 px-3"><i class="fas fa-grip-vertical"></i></div>
                    <div class="w-24 h-12 bg-red-600 rounded flex items-center justify-center text-white text-[10px] font-bold overflow-hidden shadow-inner mr-4">
                        <span class="z-10">YOUTUBE PREMIUM</span>
                    </div>
                    <div class="flex-1">
                        <p class="text-xs text-gray-500">Banner #1630</p>
                        <p class="text-sm font-bold text-gray-800">YOUTUBE_PREMIUM_20_05_2026</p>
                    </div>
                    <button class="w-8 h-8 rounded-full text-red-500 hover:bg-red-50 flex items-center justify-center transition-colors"><i class="fas fa-times"></i></button>
                </div>
            </div>
        </div>
        
        <!-- Pesquisa para Adicionar (Direita) -->
        <div class="w-1/3 bg-gray-50 p-6">
            <h3 class="text-sm font-bold text-gray-700 uppercase mb-4"><i class="fas fa-search mr-2 text-indigo-500"></i> Buscar Banners</h3>
            
            <form class="space-y-4 mb-6 p-4 bg-white border border-gray-200 rounded-lg">
                <div><label class="block text-xs text-gray-500 mb-1">Tipo</label><select class="w-full border border-gray-300 rounded px-2 py-1.5 text-sm"><option>Todos</option><option>Game</option></select></div>
                <div><label class="block text-xs text-gray-500 mb-1">Nome</label><input type="text" class="w-full border border-gray-300 rounded px-2 py-1.5 text-sm"></div>
                <button type="button" class="w-full py-2 bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium text-sm rounded"><i class="fas fa-search mr-2"></i>Buscar</button>
            </form>
            
            <!-- Resultados -->
            <div class="space-y-2">
                <p class="text-xs font-semibold text-gray-400 uppercase">Resultados Rápidos</p>
                <div class="bg-white p-3 border border-gray-200 rounded-lg flex items-center justify-between shadow-sm">
                    <div>
                        <p class="text-xs font-bold text-gray-800 truncate w-32">SPOTIFY_08_05_2026</p>
                        <p class="text-[10px] text-gray-400">ID: 1625</p>
                    </div>
                    <button class="w-6 h-6 bg-indigo-100 hover:bg-indigo-600 hover:text-white text-indigo-600 rounded flex items-center justify-center transition-colors"><i class="fas fa-plus text-xs"></i></button>
                </div>
            </div>
        </div>
        
    </div>
"""

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>""" + prototype_data['brand_name'] + """ - Painel Admin</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
    <style>
        body { font-family: 'Inter', system-ui, sans-serif; background-color: #F3F4F6; }
        [x-cloak] { display: none !important; }
        .sidebar-scroll::-webkit-scrollbar { width: 4px; }
        .sidebar-scroll::-webkit-scrollbar-track { background: transparent; }
        .sidebar-scroll::-webkit-scrollbar-thumb { background: #4B5563; border-radius: 4px; }
    </style>
</head>
<body x-data="{ currentView: 'login', sidebarOpen: true }">
    <div x-show="currentView === 'login'" x-cloak class="fixed inset-0 z-50 bg-gray-900">
        """ + views["login"] + """
    </div>
    <div x-show="currentView !== 'login'" x-cloak class="flex h-screen overflow-hidden">
        <aside class="bg-gray-900 text-white w-64 flex-shrink-0 flex flex-col transition-transform duration-300 shadow-2xl relative z-20"
               :class="{'translate-x-0': sidebarOpen, '-translate-x-full': !sidebarOpen, 'absolute': true, 'md:relative': true, 'md:translate-x-0': sidebarOpen}">
            <div class="h-16 flex items-center px-6 bg-gray-950 border-b border-gray-800">
                <h1 class="text-xl font-bold tracking-wider">TERRA <span class="text-indigo-400 font-light">VIVO</span></h1>
            </div>
            <div class="p-6 border-b border-gray-800">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-indigo-600 flex items-center justify-center text-white font-bold shadow-lg shadow-indigo-900/50">
                        <i class="fas fa-user-tie"></i>
                    </div>
                    <div>
                        <p class="text-xs text-gray-400">Administrador</p>
                        <p class="text-sm font-semibold truncate">81021595</p>
                    </div>
                </div>
            </div>
            <nav class="flex-1 overflow-y-auto sidebar-scroll py-4">
"""

for group in prototype_data["sidebar"]:
    html_content += f"""
                <div class="px-4 mb-2">
                    <p class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2 px-2">{group['title']}</p>
                    <ul class="space-y-1">
"""
    for item in group["items"]:
        html_content += f"""
                        <li>
                            <button @click="currentView = '{item['view']}'" 
                                    class="w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm font-medium transition-colors"
                                    :class="currentView === '{item['view']}' ? 'bg-indigo-600 text-white shadow-md' : 'text-gray-300 hover:bg-gray-800 hover:text-white'">
                                <span class="flex items-center gap-3">
                                    <i class="{group['icon']} w-4 text-center opacity-70"></i>
                                    {item['title']}
                                </span>
                            </button>
                        </li>
"""
    html_content += """
                    </ul>
                </div>
"""

html_content += """
            </nav>
            <div class="p-4 bg-gray-950">
                <button @click="currentView = 'login'" class="w-full flex items-center justify-center gap-2 px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-gray-800 rounded-lg transition-colors">
                    <i class="fas fa-sign-out-alt"></i> Sair do Sistema
                </button>
            </div>
        </aside>
        <div class="flex-1 flex flex-col h-screen overflow-hidden relative z-10" :class="{'md:ml-0': sidebarOpen}">
            <header class="h-16 bg-white shadow-sm border-b border-gray-200 flex items-center justify-between px-4 lg:px-8 z-10">
                <div class="flex items-center gap-4">
                    <button @click="sidebarOpen = !sidebarOpen" class="text-gray-500 hover:text-gray-700 focus:outline-none p-2 rounded-md hover:bg-gray-100">
                        <i class="fas fa-bars text-lg"></i>
                    </button>
                </div>
            </header>
            <main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-100 p-4 lg:p-8">
                <div class="max-w-7xl mx-auto">
"""

for view_id, view_html in views.items():
    if view_id != "login":
        html_content += f"""
                    <div x-show="currentView === '{view_id}'" x-cloak x-transition.opacity.duration.300ms>
                        {view_html}
                    </div>
"""

html_content += """
                </div>
            </main>
        </div>
    </div>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated HTML successfully.")
