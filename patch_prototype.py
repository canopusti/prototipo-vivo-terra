import re

with open('build_prototype.py', 'r') as f:
    content = f.read()

multimidia_html = """
            <!-- Multimídia Tab -->
            <div x-show="tab === 'multimidia'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Gerenciamento de Arquivos Multimídia</h3>
                <div class="bg-gray-50 p-6 rounded-xl border border-gray-200 mb-8">
                    <h4 class="text-sm font-bold text-gray-700 uppercase mb-4">Adicionar Novo Recurso</h4>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                        <div>
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Idioma</label>
                            <select class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-indigo-500 outline-none"><option>PT</option></select>
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Tipo de Recurso</label>
                            <select class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-indigo-500 outline-none"><option>TODOS</option><option>ICON</option><option>BANNER</option></select>
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Arquivo</label>
                            <input type="file" class="w-full border border-gray-300 rounded-lg px-3 py-1.5 focus:ring-2 focus:ring-indigo-500 outline-none bg-white">
                        </div>
                    </div>
                    <div class="flex justify-end">
                        <button type="button" class="px-6 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 shadow-md transition-colors flex items-center gap-2"><i class="fas fa-upload"></i> Fazer Upload</button>
                    </div>
                </div>
                
                <div class="overflow-x-auto rounded-lg border border-gray-200 shadow-sm">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase">Tipo</th>
                                <th class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase">Idioma</th>
                                <th class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase">Tamanho</th>
                                <th class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase">Preview</th>
                                <th class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase">Posição</th>
                                <th class="px-6 py-3 text-right text-xs font-bold text-gray-500 uppercase">Ações</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">
                            <tr class="hover:bg-gray-50">
                                <td class="px-6 py-4 text-sm font-medium text-gray-900">ICON</td>
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">PT</td>
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">512 x 512</td>
                                <td class="px-6 py-4 text-center"><button class="text-indigo-500 hover:text-indigo-700" title="Ver Imagem"><i class="fas fa-image text-lg"></i></button></td>
                                <td class="px-6 py-4 text-center"><input type="number" class="w-16 border border-gray-300 rounded text-center px-1" value="1"></td>
                                <td class="px-6 py-4 text-right"><button class="text-red-500 hover:text-red-700"><i class="fas fa-times-circle text-lg"></i></button></td>
                            </tr>
                            <tr class="hover:bg-gray-50">
                                <td class="px-6 py-4 text-sm font-medium text-gray-900">BANNER</td>
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">PT</td>
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">1440 x 810</td>
                                <td class="px-6 py-4 text-center"><button class="text-indigo-500 hover:text-indigo-700" title="Ver Imagem"><i class="fas fa-image text-lg"></i></button></td>
                                <td class="px-6 py-4 text-center"><input type="number" class="w-16 border border-gray-300 rounded text-center px-1" value="2"></td>
                                <td class="px-6 py-4 text-right"><button class="text-red-500 hover:text-red-700"><i class="fas fa-times-circle text-lg"></i></button></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="mt-4 flex justify-end">
                    <button type="button" class="px-4 py-2 bg-gray-100 text-gray-700 font-medium rounded-lg hover:bg-gray-200 border border-gray-300 transition-colors"><i class="fas fa-sort-numeric-down mr-2"></i> Atualizar Ordem</button>
                </div>
            </div>

            <!-- Ofertas Tab -->
            <div x-show="tab === 'ofertas'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Configuração de Ofertas e Preços</h3>
                
                <form class="bg-gray-50 p-6 rounded-xl border border-gray-200 mb-8 space-y-4">
                    <h4 class="text-sm font-bold text-gray-700 uppercase mb-4">Criar Nova Oferta</h4>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-6 gap-y-4">
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Nome da Oferta</label><input type="text" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"></div>
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Descrição</label><input type="text" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"></div>
                        
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">País</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>Brasil</option></select></div>
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">MSC Serviço</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>BR VIVO STORE CLUBVALESAUDE...</option></select></div>

                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Operadora</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>VIVO BRASIL</option></select></div>
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Segmento</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>POS | CONTROLE</option></select></div>

                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Periodicidade</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>Mensal</option></select></div>
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Plataforma</label><select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>PRM</option></select></div>
                        
                        <div class="flex items-end mb-2"><label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="w-4 h-4 text-indigo-600 rounded"><span class="text-sm font-medium text-gray-700">Oferta Default</span></label></div>
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Gratuidade (dias)</label><input type="number" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none" value="0"></div>

                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Preço (sem impostos)</label><input type="number" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none" value="0"></div>
                        <div><label class="block text-xs font-semibold text-gray-500 mb-1">Preço Final (com impostos)</label><input type="number" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none" value="32.90" step="0.01"></div>
                        
                        <div class="md:col-span-2">
                            <label class="block text-xs font-semibold text-gray-500 mb-1">Texto de Renovação no Processo de Assinatura</label>
                            <input type="text" class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none">
                        </div>
                    </div>
                    
                    <div class="flex justify-end pt-4 mt-2 border-t border-gray-200">
                        <button type="button" class="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 shadow-md transition-colors flex items-center gap-2"><i class="fas fa-plus"></i> Adicionar Oferta</button>
                    </div>
                </form>

                <div class="overflow-x-auto rounded-lg border border-gray-200 shadow-sm">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th class="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase">Nome</th>
                                <th class="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase">MSC Serviço</th>
                                <th class="px-4 py-3 text-center text-xs font-bold text-gray-500 uppercase">Valor Final</th>
                                <th class="px-4 py-3 text-center text-xs font-bold text-gray-500 uppercase">Frequência</th>
                                <th class="px-4 py-3 text-center text-xs font-bold text-gray-500 uppercase">Segmento</th>
                                <th class="px-4 py-3 text-right text-xs font-bold text-gray-500 uppercase">Ações</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">
                            <tr class="hover:bg-gray-50">
                                <td class="px-4 py-4 text-sm font-medium text-gray-900">Vale Saúde Farma</td>
                                <td class="px-4 py-4 text-xs text-gray-500">BR VIVO STORE CLUBVALESAUDE...</td>
                                <td class="px-4 py-4 text-sm font-bold text-indigo-600 text-center">R$ 32,90</td>
                                <td class="px-4 py-4 text-sm text-gray-500 text-center">Mensal</td>
                                <td class="px-4 py-4 text-xs text-gray-500 text-center">POS | CONTROLE</td>
                                <td class="px-4 py-4 text-right whitespace-nowrap">
                                    <button class="text-indigo-500 hover:text-indigo-700 mr-2 p-1"><i class="fas fa-edit text-lg"></i></button>
                                    <button class="text-red-500 hover:text-red-700 p-1"><i class="fas fa-trash-alt text-lg"></i></button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Documentação Tab -->
            <div x-show="tab === 'documentacao'" style="display: none;" class="p-8">
                <h3 class="text-lg font-semibold text-gray-800 mb-6 border-b border-gray-100 pb-2">Manuais e Termos de Uso (T&C)</h3>
                
                <!-- Manual de usuario -->
                <div class="mb-8">
                    <h4 class="text-sm font-bold text-indigo-700 uppercase mb-4"><i class="fas fa-book mr-2"></i>Manual do Usuário</h4>
                    <div class="bg-gray-50 p-5 rounded-xl border border-gray-200 mb-4 flex items-end gap-4">
                        <div class="w-1/3">
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Idioma</label>
                            <select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>PT</option></select>
                        </div>
                        <div class="w-1/2">
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Arquivo PDF</label>
                            <input type="file" class="w-full border border-gray-300 rounded-lg px-3 py-1.5 outline-none bg-white">
                        </div>
                        <button class="px-6 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700"><i class="fas fa-upload mr-2"></i> Enviar</button>
                    </div>
                    <div class="border border-gray-200 rounded-lg overflow-hidden">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-100"><tr><th class="px-4 py-2 text-left text-xs font-bold text-gray-500 w-24">Idioma</th><th class="px-4 py-2 text-left text-xs font-bold text-gray-500">Arquivo</th><th class="px-4 py-2 text-right"></th></tr></thead>
                            <tbody class="bg-white">
                                <tr>
                                    <td class="px-4 py-3 text-sm font-medium">PT</td>
                                    <td class="px-4 py-3 text-sm text-indigo-600 hover:underline cursor-pointer"><i class="fas fa-file-pdf mr-2 text-red-500"></i> manual_20260915142507.pdf</td>
                                    <td class="px-4 py-3 text-right"><button class="text-red-500 hover:text-red-700"><i class="fas fa-times-circle text-lg"></i></button></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- T&C -->
                <div>
                    <h4 class="text-sm font-bold text-indigo-700 uppercase mb-4"><i class="fas fa-file-signature mr-2"></i>Termos e Condições (T&C)</h4>
                    <div class="bg-gray-50 p-5 rounded-xl border border-gray-200 mb-4 grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Idioma</label>
                            <select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>PT</option></select>
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Arquivo T&C</label>
                            <input type="file" class="w-full border border-gray-300 rounded-lg px-3 py-1.5 outline-none bg-white">
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1">Modo de Exibição</label>
                            <select class="w-full border border-gray-300 rounded-lg px-3 py-2 outline-none"><option>Mostrar TYC com seleção</option></select>
                        </div>
                        <div class="flex items-center pt-5">
                            <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="w-4 h-4 text-indigo-600 rounded"><span class="text-sm font-medium text-gray-700">T&C Pré-marcado por padrão</span></label>
                        </div>
                        <div class="col-span-2 flex justify-end pt-2 border-t border-gray-200 mt-2">
                            <button class="px-6 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700"><i class="fas fa-plus mr-2"></i> Adicionar Termo</button>
                        </div>
                    </div>
                    <div class="border border-gray-200 rounded-lg overflow-hidden">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-100"><tr><th class="px-4 py-2 text-left text-xs font-bold text-gray-500">Idioma</th><th class="px-4 py-2 text-left text-xs font-bold text-gray-500">Seleção</th><th class="px-4 py-2 text-center text-xs font-bold text-gray-500">Pré-marcado</th><th class="px-4 py-2 text-left text-xs font-bold text-gray-500">Arquivo</th><th class="px-4 py-2 text-right"></th></tr></thead>
                            <tbody class="bg-white">
                                <tr>
                                    <td class="px-4 py-3 text-sm font-medium">PT</td>
                                    <td class="px-4 py-3 text-sm text-gray-600">Com Seleção</td>
                                    <td class="px-4 py-3 text-sm text-gray-600 text-center">Não</td>
                                    <td class="px-4 py-3 text-sm text-indigo-600 hover:underline cursor-pointer"><i class="fas fa-file-pdf mr-2 text-red-500"></i> Terms63652_PT_...pdf</td>
                                    <td class="px-4 py-3 text-right"><button class="text-red-500 hover:text-red-700"><i class="fas fa-times-circle text-lg"></i></button></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
"""

# Replace the empty states div with the actual HTML
empty_states_str = """            <!-- Outras Tabs Vias Empty States -->
            <div x-show="['multimidia', 'ofertas', 'documentacao'].includes(tab)" style="display: none;" class="p-12">
                <div class="flex flex-col items-center justify-center text-gray-400 bg-gray-50 rounded-xl p-10 border-2 border-dashed border-gray-200">
                    <i class="fas fa-paint-roller text-4xl mb-4 text-gray-300"></i>
                    <h2 class="text-xl font-medium text-gray-600" x-text="'Módulo ' + tab.toUpperCase()"></h2>
                    <p class="mt-2 text-sm text-gray-500 text-center max-w-md">Esta seção é vinculada apenas ao PNO e está em construção. Aqui você poderá gerenciar as configurações exclusivas deste serviço.</p>
                </div>
            </div>"""

new_content = content.replace(empty_states_str, multimidia_html)

with open('build_prototype.py', 'w') as f:
    f.write(new_content)
